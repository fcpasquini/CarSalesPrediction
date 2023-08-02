import numpy as np
from keras.models import load_model
import streamlit as st
import joblib

def create_main_pg():
    # Create page
    st.set_page_config(page_title='Predict', page_icon=':car:', layout = 'wide')
    
    with open('./page_content/03.txt') as file:
        page_content = file.read()

    st.markdown(page_content, unsafe_allow_html=True)

dict_countries = {'Afghanistan': '0',
 'Algeria': '1',
 'American Samoa': '2',
 'Andorra': '3',
 'Angola': '4',
 'Anguilla': '5',
 'Antarctica': '6',
 'Argentina': '7',
 'Armenia': '8',
 'Aruba': '9',
 'Australia': '10',
 'Austria': '11',
 'Bahamas': '12',
 'Bahrain': '13',
 'Bangladesh': '14',
 'Belarus': '15',
 'Belgium': '16',
 'Belize': '17',
 'Benin': '18',
 'Bermuda': '19',
 'Bhutan': '20',
 'Bolivia': '21',
 'Bonaire, Sint Eustatius and Saba': '22',
 'Bosnia and Herzegovina': '23',
 'Botswana': '24',
 'Bouvet Island': '25',
 'Brazil': '26',
 'Bulgaria': '27',
 'Cambodia': '28',
 'Cameroon': '29',
 'Canada': '30',
 'Cape Verde': '31',
 'Cayman Islands': '32',
 'Central African Republic': '33',
 'Chad': '34',
 'Chile': '35',
 'China': '36',
 'Christmas Island': '37',
 'Cocos (Keeling) Islands': '38',
 'Colombia': '39',
 'Congo (Brazzaville)': '40',
 'Cook Islands': '41',
 'Costa Rica': '42',
 'Croatia': '43',
 'Curaçao': '44',
 'Czech Republic': '45',
 'Denmark': '46',
 'Djibouti': '47',
 'Dominican Republic': '48',
 'Ecuador': '49',
 'Egypt': '50',
 'El Salvador': '51',
 'Equatorial Guinea': '52',
 'Ethiopia': '53',
 'Falkland Islands': '54',
 'Faroe Islands': '55',
 'France': '56',
 'French Guiana': '57',
 'French Polynesia': '58',
 'French Southern Territories': '59',
 'Gabon': '60',
 'Gambia': '61',
 'Georgia': '62',
 'Germany': '63',
 'Ghana': '64',
 'Greece': '65',
 'Greenland': '66',
 'Grenada': '67',
 'Guadeloupe': '68',
 'Guam': '69',
 'Guatemala': '70',
 'Guernsey': '71',
 'Guinea': '72',
 'Guinea-Bissau': '73',
 'Guyana': '74',
 'Haiti': '75',
 'Heard Island and Mcdonald Islands': '76',
 'Honduras': '77',
 'Hong Kong': '78',
 'Hungary': '79',
 'Iceland': '80',
 'India': '81',
 'Indonesia': '82',
 'Iraq': '83',
 'Isle of Man': '84',
 'Israel': '85',
 'Italy': '86',
 'Jamaica': '87',
 'Japan': '88',
 'Jersey': '89',
 'Jordan': '90',
 'Kazakhstan': '91',
 'Kenya': '92',
 'Kiribati': '93',
 'Korea, South': '94',
 'Kuwait': '95',
 'Kyrgyzstan': '96',
 'Laos': '97',
 'Latvia': '98',
 'Lebanon': '99',
 'Liberia': '100',
 'Liechtenstein': '101',
 'Lithuania': '102',
 'Luxembourg': '103',
 'Macao': '104',
 'Macedonia': '105',
 'Madagascar': '106',
 'Malawi': '107',
 'Malaysia': '108',
 'Maldives': '109',
 'Mali': '110',
 'Malta': '111',
 'Marshall Islands': '112',
 'Martinique': '113',
 'Mauritania': '114',
 'Mauritius': '115',
 'Mayotte': '116',
 'Mexico': '117',
 'Micronesia': '118',
 'Moldova': '119',
 'Monaco': '120',
 'Mongolia': '121',
 'Montenegro': '122',
 'Morocco': '123',
 'Mozambique': '124',
 'Myanmar': '125',
 'Namibia': '126',
 'Nauru': '127',
 'Nepal': '128',
 'New Caledonia': '129',
 'New Zealand': '130',
 'Nicaragua': '131',
 'Niger': '132',
 'Nigeria': '133',
 'Niue': '134',
 'Norfolk Island': '135',
 'Northern Mariana Islands': '136',
 'Oman': '137',
 'Pakistan': '138',
 'Palau': '139',
 'Palestine, State of': '140',
 'Papua New Guinea': '141',
 'Paraguay': '142',
 'Peru': '143',
 'Philippines': '144',
 'Poland': '145',
 'Portugal': '146',
 'Puerto Rico': '147',
 'Qatar': '148',
 'Reunion': '149',
 'Rwanda': '150',
 'Saint Barthélemy': '151',
 'Saint Helena, Ascension and Tristan da Cunha': '152',
 'Saint Kitts and Nevis': '153',
 'Saint Lucia': '154',
 'Saint Martin': '155',
 'Saint Pierre and Miquelon': '156',
 'Saint Vincent and The Grenadines': '157',
 'Samoa': '158',
 'San Marino': '159',
 'Sao Tome and Principe': '160',
 'Saudi Arabia': '161',
 'Senegal': '162',
 'Serbia': '163',
 'Seychelles': '164',
 'Sierra Leone': '165',
 'Singapore': '166',
 'Sint Maarten': '167',
 'Slovakia': '168',
 'Slovenia': '169',
 'Solomon Islands': '170',
 'Somalia': '171',
 'South Africa': '172',
 'South Georgia and The South Sandwich Islands': '173',
 'South Sudan': '174',
 'Sri Lanka': '175',
 'Sudan': '176',
 'Suriname': '177',
 'Switzerland': '178',
 'Syria': '179',
 'Taiwan': '180',
 'Tanzania': '181',
 'Thailand': '182',
 'Timor-Leste': '183',
 'Togo': '184',
 'Tokelau': '185',
 'Tonga': '186',
 'Trinidad and Tobago': '187',
 'Tunisia': '188',
 'Turkey': '189',
 'Turkmenistan': '190',
 'Turks and Caicos Islands': '191',
 'Tuvalu': '192',
 'Uganda': '193',
 'Ukraine': '194',
 'United Arab Emirates': '195',
 'United Kingdom (Great Britain)': '196',
 'United States': '197',
 'United States Minor Outlying Islands': '198',
 'Uruguay': '199',
 'Vanuatu': '200',
 'Venezuela': '201',
 'Vietnam': '202',
 'Virgin Islands, British': '203',
 'Virgin Islands, United States': '204',
 'Wallis and Futuna': '205',
 'Western Sahara': '206',
 'Yemen': '207',
 'Zimbabwe': '208',
 'Marlal': '209',
 'Åland Islands': '210'}

def return_gender_number(gender):
    dict_gender = {'0 - Female':0, '1 - Male':1, '2 - Other':2}
    return dict_gender[gender]

def return_country_array(user_country):

    country_number = dict_countries[user_country]

    country_column_name = 'Country_' + country_number

    countries_array = np.array([])

    countries_columns = ['Country_1', 'Country_10', 'Country_100', 'Country_101', 'Country_102', 'Country_103', 'Country_104', 'Country_105', 'Country_106', 'Country_107', 'Country_108', 'Country_109', 'Country_11', 'Country_110', 'Country_111', 'Country_112', 'Country_113', 'Country_114', 'Country_115', 'Country_116', 'Country_117', 'Country_118', 'Country_119', 'Country_12', 'Country_120', 'Country_121', 'Country_122', 'Country_123', 'Country_124', 'Country_125', 'Country_126', 'Country_127', 'Country_128', 'Country_129', 'Country_13', 'Country_130', 'Country_131', 'Country_132', 'Country_133', 'Country_134', 'Country_135', 'Country_136', 'Country_137', 'Country_138', 'Country_139', 'Country_14', 'Country_140', 'Country_141', 'Country_142', 'Country_143', 'Country_144', 'Country_145', 'Country_146', 'Country_147', 'Country_148', 'Country_149', 'Country_15', 'Country_150', 'Country_151', 'Country_152', 'Country_153', 'Country_154', 'Country_155', 'Country_156', 'Country_157', 'Country_158', 'Country_159', 'Country_16', 'Country_160', 'Country_161', 'Country_162', 'Country_163', 'Country_164', 'Country_165', 'Country_166', 'Country_167', 'Country_168', 'Country_169', 'Country_17', 'Country_170', 'Country_171', 'Country_172', 'Country_173', 'Country_174', 'Country_175', 'Country_176', 'Country_177', 'Country_178', 'Country_179', 'Country_18', 'Country_180', 'Country_181', 'Country_182', 'Country_183', 'Country_184', 'Country_185', 'Country_186', 'Country_187', 'Country_188', 'Country_189', 'Country_19', 'Country_190', 'Country_191', 'Country_192', 'Country_193', 'Country_194', 'Country_195', 'Country_196', 'Country_197', 'Country_198', 'Country_199', 'Country_2', 'Country_20', 'Country_200', 'Country_201', 'Country_202', 'Country_203', 'Country_204', 'Country_205', 'Country_206', 'Country_207', 'Country_208', 'Country_209', 'Country_21', 'Country_210', 'Country_22', 'Country_23', 'Country_24', 'Country_25', 'Country_26', 'Country_27', 'Country_28', 'Country_29', 'Country_3', 'Country_30', 'Country_31', 'Country_32', 'Country_33', 'Country_34', 'Country_35', 'Country_36', 'Country_37', 'Country_38', 'Country_39', 'Country_4', 'Country_40', 'Country_41', 'Country_42', 'Country_43', 'Country_44', 'Country_45', 'Country_46', 'Country_47', 'Country_48', 'Country_49', 'Country_5', 'Country_50', 'Country_51', 'Country_52', 'Country_53', 'Country_54', 'Country_55', 'Country_56', 'Country_57', 'Country_58', 'Country_59', 'Country_6', 'Country_60', 'Country_61', 'Country_62', 'Country_63', 'Country_64', 'Country_65', 'Country_66', 'Country_67', 'Country_68', 'Country_69', 'Country_7', 'Country_70', 'Country_71', 'Country_72', 'Country_73', 'Country_74', 'Country_75', 'Country_76', 'Country_77', 'Country_78', 'Country_79', 'Country_8', 'Country_80', 'Country_81', 'Country_82', 'Country_83', 'Country_84', 'Country_85', 'Country_86', 'Country_87', 'Country_88', 'Country_89', 'Country_9', 'Country_90', 'Country_91', 'Country_92', 'Country_93', 'Country_94', 'Country_95', 'Country_96', 'Country_97', 'Country_98', 'Country_99']

    for column in countries_columns:
        if country_column_name == column:
            countries_array = np.append(countries_array, np.array([1]))
        else:
            countries_array = np.append(countries_array, np.array([0]))

    return countries_array

def convert_to_xarray(tuple):

    user_gender = return_gender_number(tuple[1])

    user_country_array = return_country_array(tuple[0])

    x_test = np.array([])

    list_arrays = [np.array([user_gender]), np.array([tuple[2]]), np.array([tuple[3]]), np.array([tuple[4]]), np.array([tuple[5]]), user_country_array]

    for i in list_arrays:
        x_test = np.append(x_test, i)

    x_test = x_test.reshape(1, -1)

    return x_test

def predict(_data):
    reconstructed_model = load_model('./models/')
    x_scaler = joblib.load('./models/scaler_x.save')
    y_scaler = joblib.load('./models/scaler_y.save')

    x_test = convert_to_xarray(_data)

    x_test_scaled = x_scaler.transform(x_test)

    predicted_value = reconstructed_model.predict(x_test_scaled)

    predicted_value_scaled = y_scaler.inverse_transform(predicted_value)

    return predicted_value_scaled[0][0]

countries_list = list(dict_countries.keys())
gender_list = ['0 - Female','1 - Male', '2 - Other']

create_main_pg()

user_country = st.selectbox('What is the user Country?', options = countries_list)
user_gender = st.selectbox('What is the user Gender?', options = gender_list)
user_age = st.slider('What is the user Age?', min_value = 1, max_value = 100)
user_annual_salary = st.slider('What is the user Annual Salary?', min_value = 35000, max_value = 1000000, step = 5000)
user_credit_card_debt = st.slider('What is the user Credit Card Debt?', min_value = 0, max_value = 500000, step = 5000)
user_net_worth = st.slider('What is the user Net Worth?', min_value = 0, max_value = 1000000, step = 10000)

predicted_value = predict((user_country, user_gender, user_age, user_annual_salary, user_credit_card_debt, user_net_worth))

button_click = st.button('Predict my loan:')

if button_click:
    st.text(f'The predicted value of loan approval is: {predicted_value}.')

