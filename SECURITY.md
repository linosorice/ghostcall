# Security Policy

## Reporting a vulnerability

If you find a security issue in ghostcall, please **do not open a public issue**. Report it privately via [GitHub Security Advisories](https://github.com/linosorice/ghostcall/security/advisories/new).

You should receive an acknowledgment within 72 hours. Once the issue is triaged, a fix and a coordinated disclosure timeline will be proposed.

## Supported versions

Only the latest released version receives security fixes. ghostcall follows [Semantic Versioning](https://semver.org/).

## Scope notes

ghostcall parses Python source and introspects installed packages via `importlib`. It does not execute code from the parsed source and makes no network calls. The surface most likely to produce a security-relevant issue is the handling of pathological input (malformed markdown, enormous ASTs, deeply nested attribute chains). Reports focused on those paths are especially welcome.
