# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:56:37 2014

@author: tdiethe
"""

normal_ranges = {
    'HAEMOGLOBIN': { 'low': 13.0, 'high': 17.0, 'category': 'HAEMATOLOGY', 'always_monitor': True },
    'HCT': { 'low': 0.37, 'high': 0.5, 'category': 'HAEMATOLOGY', 'always_monitor': True },
    'RED CELL COUNT' : { 'low': 4.40, 'high': 5.80, 'category': 'HAEMATOLOGY', 'always_monitor': True },
    'MCV': { 'low': 80.0, 'high': 99.0, 'category': 'HAEMATOLOGY', 'show_in_report': False },
    'MCH': { 'low': 26.0, 'high': 33.5, 'category': 'HAEMATOLOGY', 'show_in_report': False },
    'MCHC': { 'low': 30.0, 'high': 35.0, 'category': 'HAEMATOLOGY', 'show_in_report': False },
    'RDW': { 'low': 11.5, 'high':  15.0, 'category': 'HAEMATOLOGY', 'show_in_report': False },
    'PLATELET COUNT': { 'low': 150, 'high': 400, 'category': 'HAEMATOLOGY' },
    'MPV': { 'low': 7.0, 'high': 13.0, 'category': 'HAEMATOLOGY', 'show_in_report': False },
    'WHITE CELL COUNT': { 'low': 3.0, 'high': 10.0, 'category': 'HAEMATOLOGY', 'always_monitor': True },
    'Neutrophils': { 'low': 2.0, 'high': 7.5, 'category': 'HAEMATOLOGY', 'always_monitor': True },
    'Lymphocytes': { 'low': 1.2, 'high': 3.65, 'category': 'HAEMATOLOGY', 'show_in_report': False },
    'Monocytes': { 'low': 0.2, 'high': 1.0, 'category': 'HAEMATOLOGY', 'show_in_report': False },
    'Eosinophils': { 'low': 0.0, 'high': 0.4, 'category': 'HAEMATOLOGY', 'show_in_report': False },
    'Basophils': { 'low': 0.0, 'high': 0.1, 'category': 'HAEMATOLOGY', 'show_in_report': False },
    'ESR': { 'low': 1.0, 'high': 20, 'category': 'HAEMATOLOGY', 'always_monitor': True, 'notes': 'Note ref range raised in patients over 40' },
    'Active B12': { 'low': 25.1, 'high': 165.0, 'category': 'HAEMATOLOGY', 'always_monitor': True },
    'Red cell folate': { 'low': 158.0, 'high': 1099, 'category': 'HAEMATOLOGY' },
    'SODIUM': { 'low': 135.0, 'high': 145.0, 'category': 'BIOCHEMISTRY', 'always_monitor': True },
    'POTASSIUM': { 'low': 3.5, 'high': 5.1, 'category': 'BIOCHEMISTRY', 'always_monitor': True  },
    'CHLORIDE': { 'low': 98.0, 'high': 107.0, 'category': 'BIOCHEMISTRY', 'show_in_report': False },
    'BICARBONATE': { 'low': 22.0, 'high': 29.0, 'category': 'BIOCHEMISTRY', 'show_in_report': False },
    'UREA': { 'low': 1.7, 'high': 8.3, 'category': 'BIOCHEMISTRY', 'always_monitor': True },
    'CREATININE': { 'low': 66.0, 'high': 112.0, 'category': 'BIOCHEMISTRY', 'always_monitor': True },
    'estimated GFR': { 'low': 59.0, 'category': 'BIOCHEMISTRY', 'always_monitor': True, 'notes': 'For UK guidelines:www.renal.org/CKDguide/ckd.html' },
    'BILIRUBIN': { 'low': 0.0, 'high': 20.0, 'category': 'BIOCHEMISTRY' },
    'ALKALINE PHOSPHATASE': { 'low': 40.0, 'high': 129.0, 'category': 'BIOCHEMISTRY', 'always_monitor': True },
    'ASPARTATE TRANSFERASE': { 'low': 0.0, 'high': 37.0, 'category': 'BIOCHEMISTRY', 'always_monitor': True },
    'ALANINE TRANSFERASE': { 'low': 10.0, 'high': 50.0, 'category': 'BIOCHEMISTRY', 'always_monitor': True },
    'LDH': { 'low': 135.0, 'high': 225.0, 'category': 'BIOCHEMISTRY', 'always_monitor': True },
    'CK': { 'low': 38.0, 'high': 204.0, 'category': 'BIOCHEMISTRY', 'always_monitor': True },
    'GAMMA GT': { 'low': 10.0, 'high': 71.0, 'category': 'BIOCHEMISTRY' },
    'TOTAL PROTEIN': { 'low': 63.0, 'high': 83.0, 'category': 'BIOCHEMISTRY', 'show_in_report': False },
    'ALBUMIN': { 'low': 34.0, 'high': 50.0, 'category': 'BIOCHEMISTRY', 'show_in_report': False },
    'GLOBULIN': { 'low': 19.0, 'high': 35.0, 'category': 'BIOCHEMISTRY', 'show_in_report': False  },
    'CALCIUM': { 'low': 2.15, 'high': 2.55, 'category': 'BIOCHEMISTRY', 'always_monitor': True },
    'PHOSPHATE': { 'low': 0.87, 'high': 1.45, 'category': 'BIOCHEMISTRY', 'show_in_report': False  },
    'URIC ACID': { 'low': 266.0, 'high': 474, 'category': 'BIOCHEMISTRY', 'show_in_report': False  },
    'FASTING BLOOD GLUCOSE': { 'low': 3.9, 'high': 5.8, 'category': 'BIOCHEMISTRY' },
    'FASTING TRIGLYCERIDES': { 'high': 2.3, 'category': 'BIOCHEMISTRY' },
    'FASTING CHOLESTEROL': { 'high': 5.0, 'category': 'BIOCHEMISTRY' },
    'RANDOM BLOOD GLUCOSE (FL)': { 'high': 7.8, 'category': 'BIOCHEMISTRY' }, 
    'TRIGLYCERIDES': { 'high': 2.26, 'category': 'BIOCHEMISTRY' },
    'CHOLESTEROL': { 'high': 5.0, 'category': 'BIOCHEMISTRY' },   
    'HDL CHOLESTEROL': { 'low': 0.9, 'high': 1.5, 'category': 'BIOCHEMISTRY' },
    'HDL % of total': { 'low': 20.0, 'category': 'BIOCHEMISTRY' },
    'LDL CHOLESTEROL': { 'high': 3.0, 'category': 'BIOCHEMISTRY' },
    'IRON': { 'low': 10.6, 'high': 28.3, 'category': 'BIOCHEMISTRY', 'always_monitor': True },
    'T.I.B.C': { 'low': 41.0, 'high': 77.0, 'category': 'BIOCHEMISTRY', 'always_monitor': True },
    'TRANSFERRIN SATURATION': { 'low': 20.0, 'high': 55.0, 'category': 'BIOCHEMISTRY', 'always_monitor': True },
    'FERRITIN': { 'low': 30, 'high': 400.0, 'category': 'BIOCHEMISTRY', 'always_monitor': True },
    'C Reactive protein': { 'high': 5.0, 'category': 'BIOCHEMISTRY', 'always_monitor': True },
    'Somatomedin-C (Igf-1)': { 'low': 11.6, 'high': 31.3, 'category': 'BIOCHEMISTRY' },
    'TOTAL THYROXINE(T4)': { 'low': 59.0, 'high': 154.0, 'category': 'ENDOCRINOLOGY' },
    'THYROID STIMULATING HORMONE': { 'low': 0.27, 'high': 4.2, 'category': 'ENDOCRINOLOGY' },
    'TRIIODOTHYRONINE(T3)': { 'low': 1.3, 'high': 3.1, 'category': 'ENDOCRINOLOGY' },
    'TESTOSTERONE': { 'low': 7.6, 'high': 31.4, 'category': 'ENDOCRINOLOGY', 'always_monitor': True, 'notes': 'Reference Ranges apply to adults' },
    'CORTISOL': { 'category': 'ENDOCRINOLOGY', 'notes': 'Ref.ranges: 9 am 171 to 536 : Midnight <140', 'always_monitor': True },
    'Mineral screen': { 'category': 'SPECIAL PATHOLOGY', 'show_in_report': False },
    'Calcium - Serum': { 'low': 2.16, 'high': 2.62, 'category': 'SPECIAL PATHOLOGY' },
    'Iron - Serum': { 'low': 7.2, 'high': 28.7, 'category': 'SPECIAL PATHOLOGY' },
    'Chromium - Serum': { 'high': 1.0, 'category': 'SPECIAL PATHOLOGY' },
    'Copper - Serum': { 'low': 11.0, 'high': 22.0, 'category': 'SPECIAL PATHOLOGY' },
    'Magnesium - Serum': { 'low': 0.75, 'high': 1.00, 'category': 'SPECIAL PATHOLOGY' },
    'Manganese - Serum': { 'high': 3.2, 'category': 'SPECIAL PATHOLOGY' },
    'Zinc - Serum': { 'low': 700.0, 'high': 1200, 'category': 'SPECIAL PATHOLOGY' },
    'TOTAL ANTIOXIDANT ACTIVITY': { 'low': 1.32, 'high': 1.58, 'category': 'SPECIAL PATHOLOGY' },
    'Omega 6 / Omega 3 EFA': { 'category': 'SPECIAL PATHOLOGY' },
    'ARA Omega-6/EPA Omega-3 ratio': { 'low': 1.5, 'high': 3.0, 'optimal': 2.0, 'category': 'SPECIAL PATHOLOGY', 'notes': 'Comment: To achieve optimal ARA/EPA ratio the recommendation is 1 g of EPA daily.' },
}

def show_in_report(title):
    """
    Whether to show this one in the report
    """
    if title in normal_ranges:
        if 'show_in_report' in normal_ranges[title]:
            return normal_ranges[title]['show_in_report']
        else:
            return True
    else:
        return True # False??

def get_normal_range(title):
    """
    Get the normal range for the title
    """
    if title in normal_ranges:
        item = normal_ranges[title]
        if 'low' in item:
            if 'high' in item:
                return str(item['low']) + ' - ' + str(item['high'])
            else:
                return '>' + str(item['low'])
        else:
            if 'high' in item:
                return '<' + str(item['high'])
            else:
                return item['notes'] if 'notes' in item else 'N/A'
    else:
        return 'N/A'
        
def get_priority(title, value):
    """
    Get priorty (Action/Normal/Monitor/OK/OK-high)
    """
    if title in normal_ranges:
        item = normal_ranges[title]
        priority = ['OK', 'Normal']
        if 'high' in item and value > item['high']:
            return ['Action', 'High']
        if 'low' in item:
            if value < item['low']:
                return ['Action', 'Low']
            if 'high' in item:
                rng = item['high'] - item['low']
                if (value - item['low']) < rng * 0.25:
                    priority = ['OK', 'Low']
                if (item['high'] - value) < rng * 0.25:
                    priority = ['OK', 'High']
        if 'always_monitor' in item and item['always_monitor']:
            priority[0] = 'Monitor'
        return priority
        
def get_additional_info(obs):
    """
    Get additional information for the observation
    """
    title = obs['identifier']['title']
    obs['normal_range'] = get_normal_range(title)
    obs['show_in_report'] = show_in_report(title)
    obs['title'] = title.title() if len(title) > 3 else title
    obs['priority'] = get_priority(title, float(obs['value']))