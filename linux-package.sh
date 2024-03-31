mkdir -p Distribution/Linux/package/opt && cp -r dist/earquiz-frequencies Distribution/Linux/package/opt

# Change permissions
find Distribution/Linux/package/opt/earquiz-frequencies -type f -exec chmod 644 -- {} +
find Distribution/Linux/package/opt/earquiz-frequencies -type d -exec chmod 755 -- {} +
find Distribution/Linux/package/usr/share -type f -exec chmod 644 -- {} +
chmod +x Distribution/Linux/package/opt/earquiz-frequencies/earquiz-frequencies
