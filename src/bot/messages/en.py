# Английские тексты
START_TEXT = (
    "👋 Welcome, @{username}! 🌟\n\n"
    "Your personal assistant 🤖 is ready to help. Use /help:\n\n"
)

HELP_TEXT = (
    "🤖 <b>@YourAssistent Support Menu</b>\n\n"
    "/start - Start/restart the bot\n"
    "/help - Support menu\n"
    "/about - Information about our company\n"
)

ABOUT_TEXT = "🎒<b>I'm an assistant bot for user identification by veins!</b>"

VERIFICATION_TEXT = (
    "🔐 <b>Verification Process</b>\n\n"
    "To complete the verification, please follow these steps:\n"
    "1. Place your hand on the scanner\n"
    "2. Wait for the scan to complete\n"
    "3. Receive your verification results\n\n"
    "If you have any questions, use /help"
)

ADD_USER_NAME_PROMPT = (
    "👤 <b>Adding a new user</b>\n\n"
    "Please enter the name of the new user:"
)

ADD_USER_PHOTOS_PROMPT = (
    "📸 <b>Adding photos</b>\n\n"
    "Please send 1 or more photos of the user's hand.\n"
    "You can send multiple photos at once."
)

ADD_USER_NO_PHOTOS = (
    "⚠️ <b>No photos detected</b>\n\n"
    "Please send at least one photo of the user's hand."
)

ADD_USER_SUCCESS = (
    "✅ <b>User added successfully!</b>\n\n"
    "User <b>{name}</b> has been added to the system."
)
