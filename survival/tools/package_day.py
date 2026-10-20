"""python3 package_day.py <deck_dir> <out_zip>  -- zip all .pptx/.md/.txt in deck_dir flat, ASCII names only."""
import sys, os, zipfile
d, out = sys.argv[1], sys.argv[2]
with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
    for f in sorted(os.listdir(d)):
        if f.endswith(('.pptx', '.md', '.txt')):
            assert f.isascii(), f
            z.write(os.path.join(d, f), f)
assert zipfile.ZipFile(out).testzip() is None
print('zip ok', out, os.path.getsize(out))
