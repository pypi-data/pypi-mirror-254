# Internal tool

## Dependencies:

- Helm
- yq

## Info

If the DOCKER_HOST environment variable is set, it will use that Docker Engine to perform the pull/push requests.

## Sample Usage:

```
otimages push -v 24.1.0 --repository random.containerhub.tld --langpacks --include otxecm-init --exclude otxecm-init-lang-es

**SOURCEREPO**/released/otxecm-init-lang-ar:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-cs-cz:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-da-dk:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-de:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-fi-fi:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-fr:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-he:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-it:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-iw:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-ja:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-kk-kz:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-ko-kr:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-nb-no:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-nl:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-pl-pl:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-pt:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-ru-ru:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-sv:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-tr-tr:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-uk-ua:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-zh-cn:24.1.0
**SOURCEREPO**/released/otxecm-init-lang-zh-tw:24.1.0

Push Images to repository:
random.containerhub.tld/otxecm-init-lang-ar:24.1.0
random.containerhub.tld/otxecm-init-lang-cs-cz:24.1.0
random.containerhub.tld/otxecm-init-lang-da-dk:24.1.0
random.containerhub.tld/otxecm-init-lang-de:24.1.0
random.containerhub.tld/otxecm-init-lang-fi-fi:24.1.0
random.containerhub.tld/otxecm-init-lang-fr:24.1.0
random.containerhub.tld/otxecm-init-lang-he:24.1.0
random.containerhub.tld/otxecm-init-lang-it:24.1.0
random.containerhub.tld/otxecm-init-lang-iw:24.1.0
random.containerhub.tld/otxecm-init-lang-ja:24.1.0
random.containerhub.tld/otxecm-init-lang-kk-kz:24.1.0
random.containerhub.tld/otxecm-init-lang-ko-kr:24.1.0
random.containerhub.tld/otxecm-init-lang-nb-no:24.1.0
random.containerhub.tld/otxecm-init-lang-nl:24.1.0
random.containerhub.tld/otxecm-init-lang-pl-pl:24.1.0
random.containerhub.tld/otxecm-init-lang-pt:24.1.0
random.containerhub.tld/otxecm-init-lang-ru-ru:24.1.0
random.containerhub.tld/otxecm-init-lang-sv:24.1.0
random.containerhub.tld/otxecm-init-lang-tr-tr:24.1.0
random.containerhub.tld/otxecm-init-lang-uk-ua:24.1.0
random.containerhub.tld/otxecm-init-lang-zh-cn:24.1.0
random.containerhub.tld/otxecm-init-lang-zh-tw:24.1.0
Are you sure you want to push to random.containerhub.tld/? [y/N]:

```

# Help:

```sh
otimages --help
Usage: otimages [OPTIONS] COMMAND [ARGS]...

╭─ Options ───────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                         │
│ --show-completion             Show completion for the current shell, to copy it or customize    │
│                               the installation.                                                 │
│ --help                        Show this message and exit.                                       │
╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────╮
│ list                                                                                            │
│ pull                                                                                            │
│ push                                                                                            │
╰─────────────────────────────────────────────────────────────────────────────────────────────────╯

```

```bash
otimages list --help
otimages pull --help
otimages push --help
```
