API_DOMAIN = "i.instagram.com"

# Instagram 134.0.0.26.121
# Android (26/8.0.0;
# 480dpi; 1080x1920; Xiaomi;
# MI 5s; capricorn; qcom; en_US; 205280538)
USER_AGENT_BASE = (
    "Instagram {app_version} "
    "Android ({android_version}/{android_release}; "
    "{dpi}; {resolution}; {manufacturer}; "
    "{model}; {device}; {cpu}; {locale}; {version_code})"
)
# Instagram 76.0.0.15.395 (iPhone9,2; iOS 10_0_2; en_US; en-US; scale=2.61; 1080x1920) AppleWebKit/420+
# Instagram 208.0.0.32.135 (iPhone; iOS 14_7_1; en_US; en-US; scale=2.61; 1080x1920) AppleWebKit/605.1.15

SOFTWARE = (
    "{model}-user+{android_release}+OPR1.170623.032+V10.2.3.0.OAGMIXM+release-keys"
)

# QUERY_HASH_PROFILE = 'c9100bf9110dd6361671f113dd02e7d6'
# QUERY_HASH_MEDIAS = '42323d64886122307be10013ad2dcc44'
# QUERY_HASH_IGTVS = 'bc78b344a68ed16dd5d7f264681c4c76'
# QUERY_HASH_STORIES = '5ec1d322b38839230f8e256e1f638d5f'
# QUERY_HASH_HIGHLIGHTS_FOLDERS = 'ad99dd9d3646cc3c0dda65debcd266a7'
# QUERY_HASH_HIGHLIGHTS_STORIES = '5ec1d322b38839230f8e256e1f638d5f'
# QUERY_HASH_FOLLOWERS = 'c76146de99bb02f6415203be841dd25a'
# QUERY_HASH_FOLLOWINGS = 'd04b0a864b4b54837c0d870b0e77e076'
# QUERY_HASH_HASHTAG = '174a5243287c5f3a7de741089750ab3b'
# QUERY_HASH_COMMENTS = '33ba35852cb50da46f5b5e889df7d159'
# QUERY_HASH_TAGGED_MEDIAS = 'be13233562af2d229b008d2976b998b5'

LOGIN_EXPERIMENTS = "ig_android_reg_nux_headers_cleanup_universe,ig_android_device_detection_info_upload,ig_android_nux_add_email_device,ig_android_gmail_oauth_in_reg,ig_android_device_info_foreground_reporting,ig_android_device_verification_fb_signup,ig_android_direct_main_tab_universe_v2,ig_android_passwordless_account_password_creation_universe,ig_android_direct_add_direct_to_android_native_photo_share_sheet,ig_growth_android_profile_pic_prefill_with_fb_pic_2,ig_account_identity_logged_out_signals_global_holdout_universe,ig_android_quickcapture_keep_screen_on,ig_android_device_based_country_verification,ig_android_login_identifier_fuzzy_match,ig_android_reg_modularization_universe,ig_android_security_intent_switchoff,ig_android_device_verification_separate_endpoint,ig_android_suma_landing_page,ig_android_sim_info_upload,ig_android_smartlock_hints_universe,ig_android_fb_account_linking_sampling_freq_universe,ig_android_retry_create_account_universe,ig_android_caption_typeahead_fix_on_o_universe"

SUPPORTED_CAPABILITIES_OLD = [
    {
        "value": "119.0,120.0,121.0,122.0,123.0,124.0,125.0,126.0,127.0,128.0,129.0,130.0,131.0,132.0,133.0,134.0,135.0,136.0,137.0,138.0,139.0,140.0,141.0,142.0",
        "name": "SUPPORTED_SDK_VERSIONS",
    },
    {"value": "14", "name": "FACE_TRACKER_VERSION"},
    {"value": "ETC2_COMPRESSION", "name": "COMPRESSION"},
    {"value": "gyroscope_enabled", "name": "gyroscope"},
]

SUPPORTED_CAPABILITIES = [
    {'name': 'SUPPORTED_SDK_VERSIONS', 'value': '133.0,134.0,135.0,136.0,137.0,138.0,139.0,140.0,141.0,142.0,143.0,144.0,145.0,146.0,147.0,148.0,149.0,150.0,151.0,152.0,153.0,154.0,155.0,156.0,157.0,158.0,159.0,160.0,161.0,162.0,163.0,164.0,165.0,166.0,167.0,168.0,169.0,170.0,171.0,172.0,173.0,174.0,175.0,176.0'}, 
    {'name': 'FACE_TRACKER_VERSION', 'value': '14'}, 
    {'name': 'segmentation', 'value': 'segmentation_enabled'}, 
    {'name': 'COMPRESSION', 'value': 'ETC2_COMPRESSION'}, 
    {'name': 'world_tracker', 'value': 'world_tracker_enabled'}, 
    {'name': 'gyroscope', 'value': 'gyroscope_enabled'}
    ]


MAX_RETRIES = 10