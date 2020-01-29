# uris for use in fetch.py
# Format: ( name, desc, uri )

# Note that <name> will be used as a filename and even directory name
# for files that get unzipped by download_and_extract_uris()

uris=(
    ( 'EN.ATM.CO2E.PC', 'CO2 emissions (metric tons per capita)',
        'http://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.PC?downloadformat=csv' ),
    ( 'IP.PAT.NRES', 'Patent applications, nonresidents',
        'http://api.worldbank.org/v2/en/indicator/IP.PAT.NRES?downloadformat=csv' ),
    ( 'IP.PAT.RESD','Patent applications, residents',
        'http://api.worldbank.org/v2/en/indicator/IP.PAT.RESD?downloadformat=csv' ),
    ( 'NY.GDP.MKTP.CD','GDP (current US$)',
        'http://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=csv' ),
    ( 'SP.DYN.LE00.IN','Life expectancy at birth, total (years)',
        'http://api.worldbank.org/v2/en/indicator/SP.DYN.LE00.IN?downloadformat=csv' ),
    ( 'SP.POP.TOTL','Population, total',
        'http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv' ),
    ( 'TX.VAL.TECH.MF.ZS','High-technology exports (%)',
        'http://api.worldbank.org/v2/en/indicator/TX.VAL.TECH.MF.ZS?downloadformat=csv' ),
)
