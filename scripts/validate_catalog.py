#!/usr/bin/env python3
"""Validador offline da curadoria e da identidade visual para GitHub."""
from __future__ import annotations

import csv
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "catalog" / "repositorios.csv"
REQUIRED = {
    "repository", "url", "primary_domain", "artifact_type",
    "tier", "verification", "curation_note", "checked_on",
}
VALID_TIERS = {"A", "B", "C"}
VALID_VERIFICATION = {"repo_confirmado", "repo_confirmado_readme"}
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_REF = re.compile(r"\b(?:href|src)\s*=\s*[\"']([^\"']+)[\"']", re.IGNORECASE)


def validate_registry(errors: list[str]) -> int:
    if not REGISTRY.is_file():
        errors.append("CSV ausente: catalog/repositorios.csv")
        return 0

    with REGISTRY.open(encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        missing = REQUIRED - set(reader.fieldnames or ())
        if missing:
            errors.append(f"Colunas ausentes no CSV: {sorted(missing)}")
            return 0
        seen = set()
        count = 0
        for row_num, row in enumerate(reader, start=2):
            count += 1
            name = (row["repository"] or "").strip()
            slug = name.casefold()
            if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", name):
                errors.append(f"Linha {row_num}: owner/repo invalido: {name!r}")
            if slug in seen:
                errors.append(f"Linha {row_num}: duplicado: {name}")
            seen.add(slug)
            expected_url = f"https://github.com/{name}"
            if (row["url"] or "").rstrip("/").casefold() != expected_url.casefold():
                errors.append(f"Linha {row_num}: URL divergente para {name}")
            if row["tier"] not in VALID_TIERS:
                errors.append(f"Linha {row_num}: tier invalido")
            if row["verification"] not in VALID_VERIFICATION:
                errors.append(f"Linha {row_num}: verification invalida")
            if not row["primary_domain"] or not row["artifact_type"] or not row["curation_note"]:
                errors.append(f"Linha {row_num}: metadados obrigatorios vazios")
            try:
                date.fromisoformat(row["checked_on"])
            except (ValueError, TypeError):
                errors.append(f"Linha {row_num}: checked_on invalido")
    return count


def validate_local_links(errors: list[str]) -> int:
    total = 0
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        data = md.read_text(encoding="utf-8")
        refs = [m.group(1).strip().split(" ", 1)[0].strip("<>") for m in MARKDOWN_LINK.finditer(data)]
        refs.extend(m.group(1) for m in HTML_REF.finditer(data))
        for target in refs:
            if not target or target.startswith("#"):
                continue
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or target.startswith("//"):
                continue
            path = unquote(parsed.path)
            if not path or path.startswith("/"):
                continue
            total += 1
            resolved = (md.parent / path).resolve()
            if not resolved.is_relative_to(ROOT):
                errors.append(f"{md.relative_to(ROOT)}: link sai do repositorio: {target}")
            elif not resolved.exists():
                errors.append(f"{md.relative_to(ROOT)}: link quebrado: {target}")
    return total


def validate_svg_assets(errors: list[str]) -> int:
    count = 0
    for svg in (ROOT / "docs" / "assets").glob("*.svg"):
        count += 1
        try:
            root = ElementTree.parse(svg).getroot()
        except ElementTree.ParseError as exc:
            errors.append(f"{svg.relative_to(ROOT)}: SVG XML invalido: {exc}")
            continue
        if root.tag != "{http://www.w3.org/2000/svg}svg":
            errors.append(f"{svg.relative_to(ROOT)}: elemento raiz nao e SVG")
        for node in root.iter():
            tag = node.tag.split("}")[-1].lower()
            if tag in {"script", "foreignobject", "image"}:
                errors.append(f"{svg.relative_to(ROOT)}: elemento nao permitido: {tag}")
            for name, value in node.attrib.items():
                n = name.split("}")[-1].lower()
                if n.startswith("on") or (n in {"href", "src"} and (value.startswith("http") or value.startswith("data:"))):
                    errors.append(f"{svg.relative_to(ROOT)}: atributo ativo ou recurso externo")
    return count


def main() -> int:
    errors: list[str] = []
    records = validate_registry(errors)
    links = validate_local_links(errors)
    assets = validate_svg_assets(errors)
    print(f"Curadoria: {records} registros, {links} links locais, {assets} SVGs examinados.")
    if errors:
        print("\n".join(f"ERROR: {item}" for item in errors), file=sys.stderr)
        return 1
    print("PASS: catalogo sem duplicacoes, links validos e SVGs passivos bem formados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
