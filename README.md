# nostrpy

A python library and reference CLI tool implementing the [nostr](https://github.com/fiatjaf/nostr/) protocol. Still very much a work in progress.

- [x] BIP-340 Schnorr signatures using the reference Python implementation
- [ ] Complete Pythonic API for the nostr protocol
- [ ] Reference CLI tool implementing the nostr client and server

Supports Python 3.7 and up.

## Usage

```bash
$ pip install nostr
```

## Dev

For development it's best to use `pipenv`:

```bash
$ pipenv install -d
$ pipenv run test
```
