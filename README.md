# domainstemmer
PoC Python module for stemming domain names. Reduces domain names to a form that is directly under a public suffix. Great for de-duping blacklists and summarizing assets when doing OSINT.

The master list of public suffixes can be found in https://publicsuffix.org/.

## Installation

To install, just clone, and run `pip install .`
```bash
git clone https://github.com/penafieljlm/domainstemmer.git
cd domainstemmer
pip install .
```

## Usage

To use, just import and call the `stem` function.
```python
>>> import domainstemmer
>>> domainstemmer.stem('ph.login.example.com')
'example.com'
```
