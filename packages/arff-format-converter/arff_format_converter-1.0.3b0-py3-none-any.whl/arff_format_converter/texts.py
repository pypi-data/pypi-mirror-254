help_message = '''Convert ARFF files to different formats.
The arff-converter tool allows you to convert ARFF files to various output formats. Below are the details:

SYNOPSIS:
    arff-format-converter -f <file> -o <output_folder> -fmt <output_format>

EXAMPLES:
    arff-format-converter -f data.arff -o output -fmt json
    arff-format-converter -f data.arff -o output -fmt xml
    arff-format-converter -f data.arff -o output -fmt csv
    arff-format-converter -f data.arff -o output -fmt xlsx
    arff-format-converter -f data.arff -o output -fmt orc

OPTIONS:
    -f, --file      Path to the ARFF file.
    -o, --output    Path to the output folder.
    -fmt, --format  Output format: 'xml', 'json', 'csv', 'xlsx', 'orc'.

SUPPORTED FORMATS:
    - ARFF (input)
    - XML (output)
    - JSON (output)
    - CSV (output)
    - XLSX (output)
    - ORC (Apache ORC format) (output)

AUTHOR:
    Written by Shani Sinojiya <https://www.shanisinojiya.com>.

REPORTING BUGS:
    Report bugs to <https://github.com/Shani-Sinojiya/arff-format-converter/issues>

COPYRIGHT:
    Copyright © 2024
    License: GPLv3+ - GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.
'''

bottom_msg = '''SUPPORTED FORMATS:
    - ARFF (input)
    - XML (output)
    - JSON (output)
    - CSV (output)
    - XLSX (output)
    - ORC (Apache ORC format) (output)

AUTHOR:
    Written by Shani Sinojiya <https://www.shanisinojiya.com>.

REPORTING BUGS:
    Report bugs to <https://github.com/Shani-Sinojiya/arff-format-converter/issues>

COPYRIGHT:
    Copyright © 2024
    License: GPLv3+ - GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.'''
