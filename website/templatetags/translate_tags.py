from typing import Optional
from django import template


register = template.Library()


# =========================================================
# OFFLINE HINDI TRANSLATIONS
# =========================================================

HINDI_TRANSLATIONS = {

    # Navigation
    "Home": "मुखपृष्ठ",
    "FAQs": "अक्सर पूछे जाने वाले प्रश्न",
    "About Us": "हमारे बारे में",
    "Our IT Products": "हमारे आईटी उत्पाद",
    "Incentive Schemes": "प्रोत्साहन योजनाएँ",
    "Annual programme": "वार्षिक कार्यक्रम",
    "Quarterly Progress Report": "त्रैमासिक प्रगति रिपोर्ट",

    # Homepage
    "WHAT'S NEW": "नवीनतम जानकारी",
    "What's New": "नवीनतम जानकारी",
    "Quick Links": "त्वरित लिंक",
    "Downloads": "डाउनलोड",
    "About": "हमारे बारे में",

    # Branding
    "Rajbhasha Portal": "राजभाषा पोर्टल",
    "National Informatics Centre (NIC)": "राष्ट्रीय सूचना विज्ञान केंद्र (एनआईसी)",
    "Ministry of Electronics & Information Technology":
        "इलेक्ट्रॉनिकी और सूचना प्रौद्योगिकी मंत्रालय",
    "Government of India": "भारत सरकार",
    "Welcome to Rajbhasha": "राजभाषा में आपका स्वागत है",

    # Login / Account
    "Login": "लॉगिन",
    "Welcome Back": "वापसी पर स्वागत है",
    "Login using your Parichay account":
        "अपने परिचय खाते का उपयोग करके लॉगिन करें",
    "Login with Parichay": "परिचय के साथ लॉगिन करें",
    "Logout": "लॉगआउट",
    
    "About Us": "हमारे बारे में",
    "Events & Highlights": "कार्यक्रम एवं मुख्य आकर्षण",

    # Registration
    "Registration": "पंजीकरण",
    "Register": "पंजीकरण करें",
    "Create Account": "खाता बनाएँ",
    "Employee Code": "कर्मचारी कोड",
    "Email": "ईमेल",
    "Password": "पासवर्ड",
    "Confirm Password": "पासवर्ड की पुष्टि करें",

    # Common actions
    "Submit": "जमा करें",
    "Save": "सहेजें",
    "Cancel": "रद्द करें",
    "Edit": "संपादित करें",
    "Delete": "हटाएँ",
    "Update": "अद्यतन",
    "View": "देखें",
    "Search": "खोजें",
    "Back": "वापस",
    "Next": "आगे",
    "Previous": "पिछला",
    "Close": "बंद करें",

    # Profile
    "Profile": "प्रोफ़ाइल",
    "Employee Profile": "कर्मचारी प्रोफ़ाइल",
    "Update Profile": "अद्यतन अपडेट करें",
    "Personal Information": "व्यक्तिगत जानकारी",

    # QPR
    "QPR": "त्रैमासिक प्रगति रिपोर्ट",
    "Quarterly Progress Report":
        "त्रैमासिक प्रगति रिपोर्ट",
    "QPR Form": "त्रैमासिक प्रगति रिपोर्ट फॉर्म",
    "Submit QPR": "त्रैमासिक प्रगति रिपोर्ट जमा करें",
    "Edit QPR": "त्रैमासिक प्रगति रिपोर्ट संपादित करें",
    "QPR Dashboard": "त्रैमासिक प्रगति रिपोर्ट डैशबोर्ड",

    # Common status/messages
    "Pending": "लंबित",
    "Approved": "स्वीकृत",
    "Rejected": "अस्वीकृत",
    "Active": "सक्रिय",
    "Inactive": "निष्क्रिय",
    "Success": "सफलता",
    "Error": "त्रुटि",
    "Warning": "चेतावनी",

    # Help
    "Help": "सहायता",
    "Getting Help": "सहायता प्राप्त करना",
    "Frequently Asked Questions": "अक्सर पूछे जाने वाले प्रश्न",

    "Admin Dashboard": "एडमिन डैशबोर्ड",
    "Manager Dashboard": "मैनेजर डैशबोर्ड",
    "HOD Dashboard": "एचओडी डैशबोर्ड",
    "User Dashboard": "उपयोगकर्ता डैशबोर्ड",
    "Backup Dashboard": "बैकअप डैशबोर्ड",
    "Dashboard":"डैशबोर्ड",
    "Account Created!": "खाता बनाया गया!",
    "Welcome. Your data is 100% encrypted and DPDP compliant.": "आपका स्वागत है। आपका डेटा 100% एन्क्रिप्टेड और डीपीडीपी के अनुरूप है।",
    "Get Started": "शुरू करें",

    "Welcome back,": "वापसी पर स्वागत है,",
    "Manage HOD groups and system approvals.": "एचओडी समूहों और सिस्टम अनुमोदनों का प्रबंधन करें।",
    "Manage system access and employee records.": "सिस्टम एक्सेस और कर्मचारी रिकॉर्ड प्रबंधित करें।",
    "Overview of your department's progress.": "अपने विभाग की प्रगति का अवलोकन करें।",
    "Manage secure database downloads.": "सुरक्षित डेटाबेस डाउनलोड प्रबंधित करें।",
    "Manage your profile and quarterly reports.": "अपनी प्रोफ़ाइल और त्रैमासिक रिपोर्ट प्रबंधित करें।",

    "HOD Statistics": "एचओडी सांख्यिकी",
    "Emp Code": "कर्मचारी कोड",
    "HOD Name": "एचओडी का नाम",
    "IP Number": "आईपी नंबर",
    "Total Employees": "कुल कर्मचारी",
    "Profile Completed": "प्रोफ़ाइल पूर्ण",
    "QPR Completed Today": "आज पूर्ण किए गए QPR",
    "Completion %": "पूर्णता %",
    "No HOD data available": "एचओडी का डेटा उपलब्ध नहीं है",

    "Quick Actions": "त्वरित कार्रवाइयाँ",
    "Events": "कार्यक्रम",
    "Manage Employees": "कर्मचारियों का प्रबंधन करें",
    "Create New HOD": "नया एचओडी बनाएँ",
    "Create New Manager": "नया मैनेजर बनाएँ",
    "Employee Detail List": "कर्मचारी विवरण सूची",
    "Office Details": "कार्यालय विवरण",
        
    "Admin Approval Requests": "एडमिन अनुमोदन अनुरोध",
    "NAME": "नाम",
    "CONTACT": "संपर्क",
    "OFFICE": "कार्यालय",
    "No admin approval requests pending.": "कोई एडमिन अनुमोदन अनुरोध लंबित नहीं है।",
    "Active System Users": "सक्रिय सिस्टम उपयोगकर्ता",
    "USERNAME": "उपयोगकर्ता नाम",
    "ROLE": "भूमिका",
    "STATUS": "स्थिति",
    "Archive": "अभिलेखित करें",
    "Archived Users Repository": "अभिलेखित उपयोगकर्ता भंडार",
    "ORIGINAL USERNAME": "मूल उपयोगकर्ता नाम",
    "ARCHIVED DATE": "अभिलेखित की तिथि",
    "No archived users found.": "कोई अभिलेखित उपयोगकर्ता नहीं मिला।",

    # HOD Dashboard
    "Management of employees and progress tracking": "कर्मचारियों का प्रबंधन और प्रगति की निगरानी",
    "QPR SUBMITTED": "QPR जमा किया गया",
    "QPR PENDING": "QPR लंबित",
    "PROFILE UPDATED": "प्रोफ़ाइल अपडेट की गई",
    "View Detail List": "विवरण सूची देखें",
    "Change Password": "पासवर्ड बदलें",

    # Manager Dashboard
    "Manager Report": "मैनेजर रिपोर्ट",
    "Certificate": "प्रमाणपत्र",
    "Profile Management": "प्रोफ़ाइल प्रबंधन",
    "Application Users": "एप्लिकेशन उपयोगकर्ता",
    "QPR Status": "QPR स्थिति",
    "EMP CODE": "कर्मचारी कोड",
    "DESIGNATION": "पदनाम",
    "Unlock": "अनलॉक करें",

    # User Dashboard
    "Edit / Freeze Profile": "प्रोफ़ाइल संपादित / फ्रीज़ करें",
    "Fill Report": "रिपोर्ट भरें",
    "View History": "इतिहास देखें",
    "Role-Based QPR": "भूमिका-आधारित QPR",
    "Fill Manager QPR": "मैनेजर QPR भरें",
    "Fill Admin QPR": "एडमिन QPR भरें",

    "Coming Soon": "जल्द आ रहा है",

    "Rajbhasha Activities": "राजभाषा गतिविधियाँ",

    "A dedicated space for Rajbhasha activities and initiatives": "राजभाषा गतिविधियों और पहलों के लिए एक समर्पित स्थान",

    "This section is currently under development. Rajbhasha activities, programmes and related information will be available here soon.": "यह अनुभाग वर्तमान में विकासाधीन है। राजभाषा गतिविधियाँ, कार्यक्रम और संबंधित जानकारी जल्द ही यहाँ उपलब्ध होंगी।",

    "Back to Home": "मुखपृष्ठ पर वापस जाएँ",

    "Hindi Keyboard": "हिंदी कीबोर्ड",
    # Office Management
    "Office Management": "कार्यालय प्रबंधन",
    "Office Code": "कार्यालय कोड",
    "State": "राज्य",
    "Office Name": "कार्यालय का नाम",
    "Office Name (Hindi)": "कार्यालय का नाम (हिंदी)",
    "English Office Name": "अंग्रेज़ी कार्यालय का नाम",
    "Hindi Office Name": "हिंदी कार्यालय का नाम",
    "Enter the unique code assigned to this office":"इस ऑफ़िस के लिए तय किया गया यूनिक कोड डालें।",
    "Create Office":"ऑफ़िस बनाएँ",

    "Search": "खोजें",
    "Highest Hindi Exam Passed": "उत्तीर्ण उच्चतम हिंदी परीक्षा",
    "All": "सभी",
    "Filter": "फ़िल्टर",
    "Reset": "रीसेट",
    "Empcode": "कर्मचारी कोड",
    "Employee Name": "कर्मचारी का नाम",

    # Office status
    "Frozen": "लॉक",
    "Editable": "संपादन योग्य",
    "Request Pending": "अनुरोध लंबित",
    "Edit Permission Approved": "संपादन अनुमति स्वीकृत",
     # Office actions
    "Freeze": "लॉक करें",
    "Request Edit Permission": "संपादन अनुमति का अनुरोध करें",
    "Save Changes": "परिवर्तन सहेजें",
     # Office edit request
    "Edit Office": "कार्यालय संपादित करें",
    "Update office names": "कार्यालय के नाम अपडेट करें",
    "Request permission to update this frozen office":"इस लॉक किए गए कार्यालय को अपडेट करने की अनुमति का अनुरोध करें",
    "Office": "कार्यालय",
    "This office is currently frozen.":"यह कार्यालय वर्तमान में लॉक है।",
    "You need Admin approval before you can edit the office names.":"कार्यालय के नाम संपादित करने से पहले Admin की अनुमति आवश्यक है।",
    "Reason for Edit Request": "संपादन अनुरोध का कारण",
    "Submit Request": "अनुरोध भेजें",
    "Edit Request Rejected": "संपादन अनुरोध अस्वीकृत",
    "Please provide enough detail for the Admin to review your request":"कृपया प्रशासक को आपके अनुरोध की समीक्षा करने के लिए पर्याप्त जानकारी प्रदान करें।",

    # Admin office edit requests
    "Office Edit Requests":"कार्यालय संपादन अनुरोध",
    "Review Manager requests for editing frozen offices":"फ़्रीज़ किए गए ऑफ़िस में बदलाव के अनुरोधों की समीक्षा करें।",
    "Pending": "लंबित",
    "Manager": "प्रबंधक",
    "Reason": "कारण",
    "Requested On": "अनुरोध दिनांक",
    "Actions": "कार्रवाइयाँ",
    "Approve": "स्वीकृत करें",
    "Reject": "अस्वीकार करें",
    "No Pending Office Edit Requests":"कोई लंबित कार्यालय संपादन अनुरोध नहीं है",
    "All Office edit permission requests have been reviewed.":"सभी कार्यालय संपादन अनुमति अनुरोधों की समीक्षा की जा चुकी है।",
    "Edit Completed": "संपादन पूर्ण",

    "Employee": "कर्मचारी",
    "Employees": "कर्मचारीगण",
    "Employee Code": "कर्मचारी कोड",
    "Employee Name": "कर्मचारी का नाम",
    "Employee Details": "कर्मचारी विवरण",
    "Employee Management": "कर्मचारी प्रबंधन",

}

NORMALIZED_HINDI_TRANSLATIONS = {
    key.strip().casefold(): value
    for key, value in HINDI_TRANSLATIONS.items()
}

@register.filter(name="t")
def translate_text(text: Optional[str], lang: str) -> str:
    """
    Offline translation filter.

    English:
        Returns the original text.

    Hindi:
        Returns the hardcoded Hindi translation when available.
        If a translation is not yet available, the original English
        text is returned instead of making an internet request.
    """

    text_str = str(text) if text is not None else ""

    if not text_str:
        return ""

    # English does not need translation
    if lang == "en":
        return text_str

    # Hindi translation from local dictionary
    if lang == "hi":
        normalized_text = text_str.strip().casefold()
        return NORMALIZED_HINDI_TRANSLATIONS.get(
            normalized_text,
            text_str
        )

    # Any unsupported language falls back to original text
    return text_str
