# G5toA4

A simple Python program that converts G5 books in A4 pages.

## Why

- You are in a Nordic country
- You want to pre-print your thesis, which is in G5 format
- You want to be _a bit_ environmental friendly, and save some paper
- You discover that 2 G5 pages may fit in the same A4 page
- Your operating system print dialog is not able to fit them without cropping
- ...
- You use this tool to get a ready-to-print A4 PDF with 2 pages per side

# Usage

Install from pypi:

```
pip install G5toA4
```

And directly execute it:

```
G5toA4 thesis.pdf
```

Optionally, specify the output file:

```
G5toA4 thesis.pdf thesis_a4.pdf
```

## Local install

Clone this repository, then:

```
pip3 install -r requirements.txt
python3 -m G5toA4 thesis.pdf
```



# License

The code in this repository is licensed under the GNU Public License v3, see [LICENSE](LICENSE) to know more.
