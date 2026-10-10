easy = [
    'Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'Egypt', 'France', 'Germany', 'Estonia',
    'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Italy', 'Japan', 'Malaysia', 'Mali', 'Mexico',
    'Netherlands', 'Nepal', 'Nigeria', 'North Korea', 'Norway', 'Philippines', 'Poland', 'Portugal',
    'Russia', 'Saudi Arabia', 'South Africa', 'South Korea', 'Spain', 'Sweden', 'Switzerland',
    'Thailand', 'Turkey', 'United Arab Emirates', 'United Kingdom', 'United States', 'Vietnam'
]

normal = [
    'Albania', 'Angola', 'Austria', 'Bangladesh', 'Bolivia', 'Belarus', 'Belgium', 'Bulgaria', 'Chile',
    'Colombia', 'Costa Rica', 'Congo', 'Laos', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Ethiopia', 'Finland', 'Fiji',
    'Georgia', 'Greece', 'Hungary', 'Iceland', 'Malta', 'Israel', 'Jordan', 'Kazakhstan', 'Kenya',
    'Chad', 'Lebanon', 'New Zealand', 'Oman', 'Pakistan', 'Qatar', 'Romania', 'Senegal','Sudan',
    'Serbia', 'Singapore', 'Kuwait', 'Panama','Slovakia', 'Slovenia', 'Sri Lanka', 'Tanzania', 'Uganda', 'Afghanistan',
    'Uruguay', 'Uzbekistan', 'Palestine', 'Bahrain', 'Algeria', 'Andorra', 'Armenia', 'Vatican','Peru', 'Cuba', 'Taiwan', 'Bahamas'
]

hard = [
    'Azerbaijan',  'Bosnia and Herzegovina',
    'Cambodia', 'Cameroon', 'Dominican Republic',
    'Ecuador', "Cote dIvoire", 'Ghana', 'Guatemala', 'Honduras', 'Jamaica', 'Kyrgyzstan',
    'Libya', 'Maldives', 'Moldova', 'Mongolia', 'Myanmar', 'Namibia', 'Nicaragua', 'Niger',
    'North Macedonia', 'Monaco', 'Paraguay', 'Rwanda', 'Saint Lucia', 
    'Syria', 'Tajikistan', 'Tunisia', 'Venezuela', 'Yemen',
    'Zambia', 'Zimbabwe', 'Kosovo', 'Timor-Leste', 'Togo', 'Tonga', 'Turkmenistan', 'Tuvalu', 
    'Seychelles', 'Somalia', 'South Sudan', 'Suriname', 'Puerto Rico', 'Benin', 'Djibouti'
]

expert = [
    'Antigua and Barbuda', 'Barbados', 'Belize', 
    'Bhutan', 'Brunei Darussalam', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Central African Republic',
    'Comoros', 'Dominica', 'Equatorial Guinea', 'Eritrea', 'Niue', 'Montserrat',
    'Eswatini', 'Gabon', 'Gambia', 'Grenada', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Tokelau',
    'Haiti', 'Kiribati',  'Lesotho', 'Liberia', 'Liechtenstein', 'Lithuania', 'Christmas Island',
    'Luxembourg', 'Madagascar', 'Malawi', 'Marshall Islands', 'Mauritania', 'Mauritius',
    'Micronesia',  'Solomon Islands', 'Montenegro', 'Morocco', 'Mozambique', 'Nauru', 'Palau', 'Saint Pierre and Miquelon', 'Svalbard and Jan Mayen',
    'Papua New Guinea', 'Trinidad and Tobago', 'Saint Kitts and Nevis','French Southern and Antarctic Lands', 'Turks and Caicos Islands',
    'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Sierra Leone', 'Northern Mariana Islands', 'Democratic Republic of the Congo'
]

all_countries = easy + normal + hard + expert


flags_map = {
    'Bangladesh': 'bg-flag.gif',
    'Clipperton Island (Non-standard)': 'ip-flag.gif',
    'Tuvalu': 'tv-flag.gif',
    'Kyrgyzstan': 'kg-flag.gif',
    'Croatia': 'hr-flag.gif',
    'Falkland Islands (Malvinas)': 'fk-flag.gif',
    'New Hebrides (Non-standard)': 'nh-flag.gif',
    'Anguilla (Non-standard FIPS)': 'av-flag.gif',
    'Eswatini': 'wz-flag.gif',
    'East Timor (Non-standard)': 'tp-flag.gif',
    'Australia': 'as-flag.gif',
    'Liberia': 'li-flag.gif',
    'Svalbard and Jan Mayen': 'sv-flag.gif',
    'Sint Maarten (Dutch part)': 'sx-flag.gif',
    'Saint Helena, Ascension and Tristan da Cunha': 'sh-flag.gif',
    'Wallis and Futuna': 'wf-flag.gif',
    'Azerbaijan': 'aj-flag.gif',
    'Slovakia': 'lo-flag.gif',
    'British Indian Ocean Territory': 'io-flag.gif',
    'India': 'in-flag.gif',
    'Cuba': 'cu-flag.gif',
    'South Africa': 'sf-flag.gif',
    'New Caledonia': 'nc-flag.gif',
    'Chad': 'cd-flag.gif',
    'Czech Republic': 'ez-flag.gif',
    'Sudan': 'su-flag.gif',
    'Luxembourg': 'lu-flag.gif',
    'Gabon': 'gb-flag.gif',
    'Afghanistan': 'af-flag.gif',
    'Tunisia': 'ts-flag.gif',
    'Northern Mariana Islands': 'cq-flag.gif',
    'Austria': 'au-flag.gif',
    'Cyprus': 'cy-flag.gif',
    'Japan': 'ja-flag.gif',
    'Puerto Rico': 'rq-flag.gif',
    'Israel': 'is-flag.gif',
    'Cameroon': 'cm-flag.gif',
    'Norway': 'no-flag.gif',
    'Burkina Faso': 'uv-flag.gif',
    'North Korea': 'kn-flag.gif',
    'Comoros': 'cn-flag.gif',
    'Argentina': 'ar-flag.gif',
    'Jersey': 'je-flag.gif',
    'Nicaragua': 'nu-flag.gif',
    'Kosovo': 'kv-flag.gif',
    'French Southern and Antarctic Lands': 'fs-flag.png',
    'Guinea-Bissau': 'pu-flag.gif',
    'Bahamas': 'bf-flag.gif',
    'Philippines': 'rp-flag.gif',
    'Saint Vincent and the Grenadines': 'vc-flag.gif',
    'Kiribati': 'kr-flag.gif',
    'San Marino': 'sm-flag.gif',
    'Mexico': 'mx-flag.gif',
    'Malta': 'mt-flag.gif',
    'Eritrea': 'er-flag.gif',
    'Niger': 'ng-flag.gif',
    'Moldova': 'md-flag.gif',
    'Mozambique': 'mz-flag.gif',
    'Peru': 'pe-flag.gif',
    'Bosnia and Herzegovina': 'bk-flag.gif',
    'Mauritania': 'mr-flag.gif',
    'Madagascar': 'ma-flag.gif',
    'Montserrat': 'mh-flag.gif',
    'China': 'ch-flag.gif',
    'Senegal': 'sg-flag.gif',
    'Ireland': 'ei-flag.gif',
    'Bahrain': 'ba-flag.gif',
    'Virgin Islands British': 'vi-flag.gif',
    'Sint Maarten': 'sk-flag.gif',
    'Lebanon': 'le-flag.gif',
    'Iraq': 'iz-flag.gif',
    'Albania': 'al-flag.gif',
    'Slovenia': 'si-flag.gif',
    'Uruguay': 'uy-flag.gif',
    'Belarus': 'bo-flag.gif',
    'Saint Pierre and Miquelon': 'sb-flag.gif',
    'Barbados': 'bb-flag.gif',
    'Botswana': 'bc-flag.gif',
    'Ecuador': 'ec-flag.gif',
    'Guinea': 'gv-flag.gif',
    'Bouvet Island': 'bv-flag.gif',
    'Antigua and Barbuda': 'ac-flag.gif',
    'Belize': 'bh-flag.gif',
    'Micronesia': 'fm-flag.gif',
    'Romania': 'ro-flag.gif',
    'Saint Lucia': 'st-flag.gif',
    'Iran': 'ir-flag.gif',
    'Malawi': 'mi-flag.gif',
    'United States Minor Outlying Islands': 'um-flag.gif',
    'Central African Republic': 'ct-flag.gif',
    'Burundi': 'by-flag.gif',
    'Nauru': 'nr-flag.gif',
    'Gibraltar': 'gi-flag.gif',
    'Taiwan': 'tw-flag.gif',
    'Sweden': 'sw-flag.gif',
    'Seychelles': 'se-flag.gif',
    'Myanmar': 'bm-flag.gif',
    'Guatemala': 'gt-flag.gif',
    'Serbia': 'ri-flag.gif',
    'Djibouti': 'dj-flag.gif',
    'Saint Barthelemy': 'tb-flag.gif',
    'Saint Kitts and Nevis': 'sc-flag.gif',
    'Morocco': 'mo-flag.gif',
    'Heard Island and McDonald Islands': 'hm-flag.gif',
    'Suriname': 'ns-flag.gif',
    'Lithuania': 'lh-flag.gif',
    'Laos': 'la-flag.gif',
    'Palestine': 'palestine-flag.gif',
    'New Zealand': 'nz-flag.gif',
    'Pakistan': 'pk-flag.gif',
    'Turkey': 'tu-flag.gif',
    'Greenland': 'gl-flag.gif',
    'Colombia': 'co-flag.gif',
    'Costa Rica': 'cs-flag.gif',
    'Lesotho': 'lt-flag.gif',
    'Dominican Republic': 'dr-flag.gif',
    'Montenegro': 'mj-flag.gif',
    'Bolivia': 'bl-flag.gif',
    'Thailand': 'th-flag.gif',
    'Togo': 'to-flag.gif',
    'Niue': 'ne-flag.gif',
    'Mongolia': 'mg-flag.gif',
    'Dominica': 'do-flag.gif',
    'Rwanda': 'rw-flag.gif',
    'South Sudan': 'od-flag.gif',
    'Democratic Republic of the Congo': 'cf-flag.gif',
    'Turkmenistan': 'tx-flag.gif',
    'Andorra': 'an-flag.gif',
    'Brunei Darussalam': 'bx-flag.gif',
    'Hong Kong': 'hk-flag.gif',
    'Saudi Arabia': 'sa-flag.gif',
    'Italy': 'it-flag.gif',
    'Guernsey': 'gk-flag.gif',
    'Ghana': 'gh-flag.gif',
    'American Samoa': 'aq-flag.gif',
    'Ethiopia': 'et-flag.gif',
    'Greece': 'gr-flag.gif',
    'Zambia': 'za-flag.gif',
    'Turks and Caicos Islands': 'tk-flag.gif',
    'Angola': 'ao-flag.gif',
    'Macao': 'mc-flag.gif',
    'France': 'fr-flag.gif',
    'Netherlands': 'nl-flag.gif',
    'Germany': 'gm-flag.gif',
    'Belgium': 'be-flag.gif',
    'North Macedonia': 'mk-flag.gif',
    'Switzerland': 'sz-flag.gif',
    'Indonesia': 'id-flag.gif',
    'Virgin Islands US': 'vq-flag.gif',
    'Bulgaria': 'bu-flag.gif',
    'Haiti': 'ha-flag.gif',
    'Namibia': 'wa-flag.gif',
    'Trinidad and Tobago': 'td-flag.gif',
    'Norfolk Island': 'nf-flag.gif',
    'Tonga': 'tn-flag.gif',
    'Finland': 'fi-flag.gif',
    'Oman': 'mu-flag.gif',
    'Kenya': 'ke-flag.gif',
    'Sierra Leone': 'sl-flag.gif',
    'Cambodia': 'cb-flag.gif',
    'Mauritius': 'mp-flag.gif',
    'Cabo Verde': 'cv-flag.gif',
    'Solomon Islands': 'bp-flag.gif',
    'Cook Islands': 'cw-flag.gif',
    'Guam': 'gq-flag.gif',
    'Zimbabwe': 'zi-flag.gif',
    'Portugal': 'po-flag.gif',
    'Samoa': 'ws-flag.gif',
    'Marshall Islands': 'rm-flag.gif',
    'Panama': 'pm-flag.gif',
    'Malaysia': 'my-flag.gif',
    'Mali': 'ml-flag.gif',
    'Faroe Islands': 'fo-flag.gif',
    'Armenia': 'am-flag.gif',
    'Iceland': 'ic-flag.gif',
    'Jamaica': 'jm-flag.gif',
    'Paraguay': 'pa-flag.gif',
    'Singapore': 'sn-flag.gif',
    'Monaco': 'mn-flag.gif',
    'Denmark': 'da-flag.gif',
    'Tokelau': 'tl-flag.gif',
    'Chile': 'ci-flag.gif',
    'Isle of Man': 'im-flag.gif',
    'Grenada': 'gj-flag.gif',
    'Jordan': 'jo-flag.gif',
    'French Polynesia': 'fp-flag.gif',
    'Uzbekistan': 'uz-flag.gif',
    'Liechtenstein': 'ls-flag.gif',
    'Brazil': 'br-flag.gif',
    'Qatar': 'qa-flag.gif',
    'Cote dIvoire': 'iv-flag.gif',
    'Kazakhstan': 'kz-flag.gif',
    'El Salvador': 'es-flag.gif',
    'Russia': 'rs-flag.gif',
    'United States': 'us-flag.gif',
    'Vatican': 'vt-flag.gif',
    'Canada': 'ca-flag.gif',
    'Honduras': 'ho-flag.gif',
    'Bermuda': 'bd-flag.gif',
    'Equatorial Guinea': 'ek-flag.gif',
    'Libya': 'ly-flag.gif',
    'Papua New Guinea': 'pp-flag.gif',
    'Palau': 'ps-flag.gif',
    'Bhutan': 'bt-flag.gif',
    'Pitcairn': 'pc-flag.gif',
    'Maldives': 'mv-flag.gif',
    'Cocos (Keeling) Islands': 'cc-flag.gif',
    'Cayman Islands (Non-standard FIPS)': 'cj-flag.gif',
    'Georgia': 'gg-flag.gif',
    'Benin': 'bn-flag.gif',
    'Tanzania': 'tz-flag.gif',
    'Somalia': 'so-flag.gif',
    'Christmas Island': 'kt-flag.gif',
    'Egypt': 'eg-flag.gif',
    'Fiji': 'fj-flag.gif',
    'Estonia': 'en-flag.gif',
    'Vietnam': 'vm-flag.gif',
    'Algeria': 'ag-flag.gif',
    'Sri Lanka': 'ce-flag.gif',
    'Poland': 'pl-flag.gif',
    'Timor-Leste': 'tt-flag.gif',
    'Aruba': 'aa-flag.gif',
    'Nigeria': 'ni-flag.gif',
    'Guyana': 'gy-flag.gif',
    'South Korea': 'ks-flag.gif',
    'Latvia': 'lg-flag.gif',
    'Uganda': 'ug-flag.gif',
    'Cocos  Islands': 'ck-flag.gif',
    'Venezuela': 've-flag.gif',
    'Nepal': 'np-flag.gif',
    'Spain': 'sp-flag.gif',
    'Kuwait': 'ku-flag.gif',
    'Gambia': 'ga-flag.gif',
    'Tajikistan': 'ti-flag.gif',
    'Hungary': 'hu-flag.gif',
    'United Kingdom': 'uk-flag.gif',
    'United Arab Emirates': 'ae-flag.gif',
    'Yemen': 'ym-flag.gif',
    'Syria': 'sy-flag.png',
    'Congo': 'cg-flag.jpg'
}




































"""
  ____ _  _  ____  _   _ 
 / ___| || |/ ___|| | | |
| |  _| || |\___ \| |_| |
| |_| |__   _|__) |  _  |
 \____|  |_||____/|_| |_|
"""
