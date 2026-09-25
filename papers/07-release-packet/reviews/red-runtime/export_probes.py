"""Harmless temp-directory tests of export inclusion and verifier boundaries.

Archived builder and verifier are intentionally vulnerable review fixtures.
Never use them to build an actual release. This script inserts only public
sentinel strings into temporary miniature packets; no private files are read.
A deterministic stub replaces only this fixture module's renderer subprocess,
so packaging regressions require no Pandoc. This does not test HTML rendering.
"""
import importlib.util
import json
from pathlib import Path
import tempfile
import stat
from types import SimpleNamespace
import zipfile

HERE=Path(__file__).resolve().parent
PACKET=HERE.parents[1]


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod


def probe(archived=True):
    builder=module(HERE/'baseline_export_builder.py' if archived else PACKET/'surfaces/build.py','build_probe')
    checker=module(HERE/'baseline_export_verifier.py' if archived else PACKET/'surfaces/verify_export.py','verify_probe')
    # Package boundary is under test, not Pandoc. Replacing this module attribute
    # does not monkeypatch the shared subprocess module used elsewhere.
    builder.subprocess=SimpleNamespace(run=lambda *args,**kwargs: SimpleNamespace(stdout='<p>Public fixture.</p>',stderr=''))
    results={}
    with tempfile.TemporaryDirectory(prefix='mcrp-export-red-') as tmp:
        root=Path(tmp);source=root/'source';output=root/'output'
        for d in ('toy_agents/results','surfaces'):(source/d).mkdir(parents=True)
        (source/'toy_agents/results/demo.json').write_text('{"scenarios":{"release_cycle":{}}}')
        (source/'surfaces/portal.html.in').write_text('<p>Synthetic fixture __TRACE_JSON__</p>')
        (source/'surfaces/site.css').write_text('body { color: black; }')
        # Stub files ensure static header links resolve in the tiny fixture.
        for rel in ('publication/blog-introduction.md','domains/README.md','reviews/COLLECTIVE.md','publication/release-assessment.md'):
            p=source/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('# Fixture\nPublic sentinel only.\n')
        builder.ROOT=source
        output.mkdir()
        (output/'untracked.txt').write_text('PUBLIC-REVIEW-SENTINEL-UNTRACKED')
        try:
            builder.build(output)
            with zipfile.ZipFile(output/'mcrp-prototype-source.zip') as z:
                included='mcrp-prototype/untracked.txt' in z.namelist()
            results['preexisting_untracked']={'build':'accepted','included_in_zip':included}
        except (ValueError,RuntimeError) as e:
            results['preexisting_untracked']={'build':'rejected','reason':str(e)}
        output2=root/'output2'
        public_fixture=root/'public-outside-source.json';public_fixture.write_text('{"sentinel":"PUBLIC-OUTSIDE-SOURCE"}')
        (source/'linked.json').symlink_to(public_fixture)
        try:
            builder.build(output2)
            results['source_symlink']={'build':'accepted','dereferenced_into_export':(output2/'linked.json').read_bytes()==public_fixture.read_bytes()}
        except (ValueError,RuntimeError) as e:
            results['source_symlink']={'build':'rejected','reason':str(e)}
        (source/'linked.json').unlink()
        clean=root/'clean';builder.build(clean)
        with zipfile.ZipFile(clean/'mcrp-prototype-source.zip','a') as z:z.writestr('../PUBLIC-EXTRA.txt','harmless')
        check=checker.verify(clean)
        results['extra_traversal_zip_member']={'verifier_passed':check['passed'],'errors':check['errors']}
        meta=root/'metadata';builder.build(meta)
        archive=meta/'mcrp-prototype-source.zip'
        with zipfile.ZipFile(archive) as z: members=[(info,z.read(info.filename)) for info in z.infolist()]
        members[0][0].create_system=3
        members[0][0].external_attr=(stat.S_IFLNK|0o777)<<16
        with zipfile.ZipFile(archive,'w') as z:
            for info,data in members:z.writestr(info,data)
        check=checker.verify(meta)
        results['symlink_zip_metadata']={'verifier_passed':check['passed'],'errors':check['errors']}
        (clean/'unexpected.bin').write_bytes(b'PUBLIC-UNINVENTORIED')
        check=checker.verify(clean)
        results['unmanifested_output']={'verifier_passed':check['passed'],'errors':check['errors']}
    return results


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--current',action='store_true');a=p.parse_args()
    print(json.dumps(probe(not a.current),indent=2))
