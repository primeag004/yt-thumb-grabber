import subprocess
import os
import zipfile

try:
    import pyaxmlparser
except ImportError:
    pyaxmlparser = None

print("1. Running Vite build...")
subprocess.run(["npx", "vite", "build"], check=True)

base_apk = os.path.join(os.path.dirname(__file__), "template.apk")
unsigned_apk = "/tmp/omnitools-unsigned.apk"
signed_apk = "omnitools-pro.apk"
public_apk = "public/omnitools-pro.apk"

# Generate key & cert if not present
key_file = "/tmp/omnitools-key.pem"
cert_file = "/tmp/omnitools-cert.pem"
if not os.path.exists(key_file) or not os.path.exists(cert_file):
    print("Generating RSA key & certificate...")
    subprocess.run([
        "openssl", "req", "-x509", "-newkey", "rsa:2048",
        "-keyout", key_file, "-out", cert_file,
        "-days", "10000", "-nodes",
        "-subj", "/CN=OmniTools Pro"
    ], check=True)

# Read resources.arsc and modify app name
with zipfile.ZipFile(base_apk, 'r') as zin:
    arsc = zin.read('resources.arsc')
    dex = zin.read('classes.dex')
    manifest = zin.read('AndroidManifest.xml')
    layout = zin.read('res/layout/activity_main.xml')

# Replace 'WebView Apk Template' with 'OmniTools Pro 1500+ '
new_name = b'OmniTools Pro 1500+ '
assert len(new_name) == len(b'WebView Apk Template')
arsc_mod = arsc.replace(b'WebView Apk Template', new_name)

print("2. Packaging Android APK with web assets...")
with zipfile.ZipFile(unsigned_apk, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
    zout.writestr('AndroidManifest.xml', manifest)
    zout.writestr('resources.arsc', arsc_mod)
    zout.writestr('classes.dex', dex)
    zout.writestr('res/layout/activity_main.xml', layout)
    
    # Custom icon
    if os.path.exists('/tmp/ic_launcher.png'):
        with open('/tmp/ic_launcher.png', 'rb') as f:
            zout.writestr('res/mipmap-xhdpi-v4/ic_launcher.png', f.read())
            
    # Add web assets from dist/
    for root, _, files in os.walk('dist'):
        for file in files:
            full_path = os.path.join(root, file)
            # Skip any existing .apk to avoid recursion
            if file.endswith('.apk'):
                continue
            rel_path = os.path.relpath(full_path, 'dist')
            apk_path = f"assets/{rel_path}"
            with open(full_path, 'rb') as f:
                zout.writestr(apk_path, f.read())

print("3. Signing APK with v1, v2, and v3 signatures...")
node_sign_script = f"""
import("node:fs").then(async ({{ readFileSync, writeFileSync }}) => {{
  const {{ ApkSigner, SigningKey }} = await import("apk_sign_ts");
  const apk = new Uint8Array(readFileSync("{unsigned_apk}"));
  const privateKey = readFileSync("{key_file}", "utf8");
  const certificate = readFileSync("{cert_file}", "utf8");
  const signer = new ApkSigner({{
    signingKey: SigningKey.fromPEM(privateKey, certificate)
  }});
  const {{ signedApk }} = await signer.sign(apk);
  writeFileSync("{signed_apk}", signedApk);
  writeFileSync("{public_apk}", signedApk);
  console.log("Successfully signed APK, output size:", signedApk.byteLength, "bytes");
}});
"""

subprocess.run(["node", "-e", node_sign_script], check=True)

# Copy to dist so preview server serves it immediately
os.makedirs("dist", exist_ok=True)
with open(signed_apk, "rb") as fin, open("dist/omnitools-pro.apk", "wb") as fout:
    fout.write(fin.read())

print("4. Verifying final signed APK...")
if pyaxmlparser:
    apk = pyaxmlparser.APK(signed_apk)
    print(f"  Package: {apk.package}")
    print(f"  App Name: {apk.application}")
    print(f"  Activities: {apk.get_activities()}")
    print(f"  Permissions: {apk.get_permissions()}")
else:
    print("  (pyaxmlparser not installed, skipping detailed manifest parse)")

with zipfile.ZipFile(signed_apk) as z:
    asset_files = [n for n in z.namelist() if n.startswith('assets/')]
    print(f"  Total files in APK: {len(z.namelist())}")
    print(f"  Web assets packaged: {len(asset_files)} (including assets/index.html)")

print("APK Build Completed Successfully!")
