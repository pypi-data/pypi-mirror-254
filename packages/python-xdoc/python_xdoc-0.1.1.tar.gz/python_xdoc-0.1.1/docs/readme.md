<div align=center>

# XDoc

</div>

This tool is for converting various document formats to PDF format. Generate PDF documents from files such as Markdown, HTML, and CSS by combining them.

## Key Features

- Generate PDFs by combining Markdown, HTML, and CSS.
- Add custom headers and footers.
- User-friendly Gradio web interface. 

## Getting started 

```sh
# Install
pip install python-xdoc

xdoc -i input_*.md -o output_file.pdf # CLI: Convert markdowns to PDF 
xdoc --webui # Web UI
xdoc --help 

Usage: 
        [Examples]

        Generate:
            From local file:
                xdoc -i in_*.html --verbose

            From remote file:
                set gist https://gist.githubusercontent.com/.../gistfile.md
                xdoc -i $gist

            Styling:
                xdoc -i in_*.html --scale 0.8 --css ' h1 { color: red }' --margin 'top bottom 50mm left right 20mm'

            Load Config:
                xdoc --config config.yaml

        Modify:
            Extract pages:
                xdoc -i in.pdf --extract 2-3

            meta
                xdoc -i in.md --meta '/Title Untitled'

        Encrypt/Decrypto:
            xdoc -i demo.pdf -o demo.encrypted.pdf --encrypto --autogen
            xdoc -i demo.encrypted.pdf -o demo.decrypted.pdf --decrypto

        Share:
            python -i $gist -o out.pdf --share mega

        [Units]

        You can use the following units for width, height, and margin options:
        - px (pixels) - Default unit., in (inches)., cm (centimeters)., mm (millimeters).

        [Formats]

        The following paper formats are available for the format option:
        - Letter, Legal, Tabloid, Ledger, A0, A1, A2, A3, A4 (default), A5

        [PDF meta]

        meta format: "/Key Value" pairs separated by space.
        - /Title, /Author, /Subject, /Author, /Keyword, /Creator, /Producer, /CreateDate,  /ModDate, /Trapped
        

Generate PDF from HTML pages.

options:
  -h, --help            show this help message and exit
  -i INPUT [INPUT ...], --input INPUT [INPUT ...]
                        Input files.
  -o OUTPUT [OUTPUT ...], --output OUTPUT [OUTPUT ...]
                        Output file path.
  --scale SCALE         Scale of the printed page | 0.8 for 80 percent.
  --displayHeaderFooter
                        Display header and footer.
  --headerTemplate HEADERTEMPLATE
                        Add header template as [url|path|content].
  --footerTemplate FOOTERTEMPLATE
                        Add footer template as [url|path|content].
  --printBackground     Print background images.
  --landscape           Use landscape paper orientation.
  --pageRanges PAGERANGES
                        Page ranges to print | '1-5,8,11-13'.
  --format FORMAT       Paper format | 'A4'.
  --width WIDTH         Paper width | '10cm'.
  --height HEIGHT       Paper height | '10mm'.
  --margin MARGIN       Margin values (e.g., 'top 10mm right 10mm')
  --css CSS             Add css as [url|path|content]
  --config CONFIG       Path to the config file.
  --emulateMedia {screen,print}
                        Type of emulate media.
  --qr QR               Add QR after link.
  --merge MERGE [MERGE ...]
                        Merge PDF files into an output file
  --extract EXTRACT     Extract pages from a PDF file (e.g., '1-3')
  --split               Split a PDF file at specified pages
  --extract-text        Extract text from a PDF file
  --redact-text REDACT_TEXT [REDACT_TEXT ...]
                        Redact text in the PDF files
  --meta META           Add meta in the format '/Key: Value'. Example: '/Title
                        Document'
  --remove-meta         Remove meta from a PDF file
  --select-meta SELECT_META [SELECT_META ...]
                        Selectively remove meta fields
  --verbose             Print parameters when verbose.
  --encrypto            Encrypt PDF file.
  --autogen             Automatically generate password for encryption.
  --decrypto            Decrypt PDF file.
  --regen               Regenerate and send recovery key for decryption.
  --webui               [WIP] Launch Gradio web UI.
  --share {mega,google_drive,slideshare}
                        Specify the cloud service to use for sharing
```

## License

This project is provided under the MIT License. See the LICENSE file for details.

## Support

For inquiries regarding support, including questions and bug reports, please use GitHub Issues.

## See also

There are other similar projects that you may be interested in:

- [single-file-cli](https://github.com/gildas-lormeau/single-file-cli) - Convert a web page to a single file.

- [monolith](https://github.com/Y2Z/monolith) - Save web pages as a single HTML file.

- [markdown-pdf](https://github.com/alanshaw/markdown-pdf) - Convert markdown to PDF with HTML and CSS.