import pypandoc

def html_to_docx(input_html_path: str, output_docx_path: str, reference_docx: str = None):
    """
    Convert an HTML file to a .docx using Pandoc.
    If reference_docx is provided, it will be used as the style/template.
    """
    extra_args = []
    if reference_docx:
        extra_args.extend(['--reference-doc', reference_docx])

    output = pypandoc.convert_file(
        source_file=input_html_path,
        to='docx',
        format='html',
        outputfile=output_docx_path,
        extra_args=extra_args
    )
    # pypandoc returns the output path when outputfile is set
    return output

if __name__ == "__main__":
    input_html  = "Python Libraries Practice/pandoc/report.html"
    output_docx = "Python Libraries Practice/pandoc/report.docx"
    # optional: pass your corporate template
    # template_docx = "corporate-style.docx"

    generated = html_to_docx(input_html, output_docx)
    print(f"Written: {generated}")
