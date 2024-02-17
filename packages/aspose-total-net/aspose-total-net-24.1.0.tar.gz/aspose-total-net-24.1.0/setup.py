from setuptools import setup

NAME = "aspose-total-net"
VERSION = "24.1.0"

REQUIRES = ["aspose-3d==24.1.0",
            "aspose-barcode-for-python-via-net==24.1",
            "aspose-cad==23.12",
            "aspose-cells-python==24.1.0",
            "aspose-diagram-python==24.1",
            "Aspose.Email-for-Python-via-NET==23.12",
            "aspose-finance==23.12",
            "aspose-imaging-python-net==23.12.0",
            "aspose-ocr-python-net==24.1.0",
            "aspose-pdf==24.1.0",
            "Aspose.Slides==24.1.0",
            "aspose-tasks==24.1.0",
            "aspose-words==24.1.0",
            "aspose-zip==24.1.0"]

"""
REQUIRES = [
            "aspose-finance"]
"""

setup(
    name=NAME,
    version=VERSION,
    description='Aspose.Total for Python via .NET is a Document Processing python class library that allows developers to work with Microsoft Word®, Microsoft PowerPoint®, Microsoft Outlook®, OpenOffice®, & 3D file formats without needing Office Automation.',
    keywords=["DOC", "DOCX", "RTF", "DOT", "DOTX", "DOTM", "DOCM FlatOPC", "FlatOpcMacroEnabled", "FlatOpcTemplate", "FlatOpcTemplateMacroEnabled", "ODT", "OTT", "WordML", "HTML", "MHTML", "PDF", "MOBI", "TXT", "PDF/A", "XPS", "OpenXPS", "PostScript (PS)", "TIFF", "JPEG", "PNG", "BMP", "SVG", "EMF", "GIF", "HtmlFixed", "PCL", "EPUB", "XamlFixed", "XamlFlow", "XamlFlowPack", "MSG", "PST", "OST", "OFT", "EML", "EMLX", "MBOX", "ICS", "VCF", "OLM", "PPT", "PPTX", "PPS", "POT", "PPSX", "PPTM", "PPSM", "POTX", "POTM", "ODP", "FBX", "STL", "OBJ", "3DS", "U3D",
              "DAE", "glTF", "ASCII", "Binary", "DRC", "RVM", "AMF", "PLY", "A3DW", "X", "DirectX", "JT", "DXF", "3MF", "ASE", "VRML", "Create", "Clone", "Render", "Compare", "Join", "Split", "Encrypt", "Digital Signature", "Mail Merge", "Reporting", "Watermark", "LINQ", "Reporting Engine", "Editor", "Merger", "Viewer", "Conversion", "Splitter", "OCR", "Translator", "Compress", "SSL", "TLS", "TNEF", "Email Attachment", "Email", "POP3", "IMAP", "iCalendar", "OleObject", "Chart", "3D", "Scene", "Triangulate", "Vulkan", "Geometry", "Camera", "Mesh", "Shape"],
    url='https://products.aspose.com/total/python-net',
    author='Aspose',
    author_email='total@aspose.com',
    packages=['aspose-total-net'],
    include_package_data=True,
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    install_requires=REQUIRES,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'License :: Other/Proprietary License'
    ],
    platforms=[
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows Vista',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.5',
)
