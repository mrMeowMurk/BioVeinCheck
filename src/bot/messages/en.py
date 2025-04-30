START_TEXT = (
    "👋 <b>Welcome, @{username}!</b> 🌟\n\n"
    "I'm your personal vein recognition assistant 🤖\n\n"
    "Here's what I can do for you:\n"
    "• Verify your identity using vein patterns 🔍\n"
    "• Manage your profile 📝\n"
    "• Provide quick access to your information 🚀\n\n"
    "Use /help to see all available commands."
)

HELP_TEXT = (
    "🤖 <b>VeinCheck Assistant Help Menu</b>\n\n"
    "Here are the commands you can use:\n\n"
    "🔹 /start - Start or restart the bot\n"
    "🔹 /help - Show this help menu\n"
    "🔹 /about - Learn more about our technology\n"
    "🔹 /verification - Verify your identity\n\n"
    "Need assistance? Feel free to ask! 😊"
)

ABOUT_TEXT = (
    "🔬 <b>About VeinCheck Technology</b>\n\n"
    "Our system uses advanced vein pattern recognition to provide secure and "
    "reliable identity verification. Here's why it's awesome:\n\n"
    "• Highly secure 🔒\n"
    "• Contactless and hygienic 🧼\n"
    "• Fast and accurate ⚡\n\n"
    "Your security is our top priority! 💪"
)

VERIFICATION_TEXT = (
    "🔐 <b>Identity Verification Process</b>\n\n"
    "Let's verify your identity quickly and securely:\n\n"
    "1. Place your hand on the scanner ✋\n"
    "2. Wait for the scan to complete ⏳\n"
    "3. Get instant verification results ✅\n\n"
    "Ready? Let's go! Use /verification to start."
)

ADD_USER_NAME_PROMPT = (
    "👤 <b>Add New User</b>\n\n"
    "Let's create a new user profile!\n\n"
    "Please enter the full name of the new user:"
)

ADD_USER_PHOTOS_PROMPT = (
    "📸 <b>Add Hand Photos</b>\n\n"
    "Now we need clear photos of the user's hand:\n\n"
    "• Take photos in good lighting 💡\n"
    "• Ensure the hand is fully visible ✋\n"
    "• You can send multiple photos at once\n\n"
    "Please send the photos now:"
)

ADD_USER_NO_PHOTOS = (
    "⚠️ <b>No Photos Received</b>\n\n"
    "We didn't receive any photos. Please try again.\n\n"
    "Remember:\n"
    "• Use good lighting 💡\n"
    "• Make sure the hand is fully visible ✋"
)

ADD_USER_SUCCESS = (
    "🎉 <b>User Added Successfully!</b>\n\n"
    "New user <b>{name}</b> has been added to the system.\n\n"
    "What's next?\n"
    "• Use /verification to test the new profile\n"
    "• Add more users with /add"
)

VERIFICATION_PHOTO_PROMPT = (
    "📸 <b>Verification Process</b>\n\n"
    "Let's verify your identity!\n\n"
    "Please send a clear photo of your hand:\n"
    "• Use good lighting 💡\n"
    "• Make sure your hand is fully visible ✋\n"
    "• Keep your hand steady for best results 🤚"
)

VERIFICATION_NO_PHOTO = (
    "⚠️ <b>No Photo Received</b>\n\n"
    "We didn't receive a photo. Please try again.\n\n"
    "Remember:\n"
    "• Use good lighting 💡\n"
    "• Make sure your hand is fully visible ✋"
)

VERIFICATION_SUCCESS = (
    "✅ <b>Verification Successful!</b>\n\n"
    "Welcome back, <b>{name}</b>!\n\n"
    "Your identity has been successfully verified.\n"
    "What would you like to do next?"
)

VERIFICATION_FAILED = (
    "❌ <b>Verification Failed</b>\n\n"
    "We couldn't verify your identity. Possible reasons:\n\n"
    "• Poor photo quality 📷\n"
    "• Hand position not optimal ✋\n"
    "• No matching profile found 🔍\n\n"
    "Please try again or contact support."
)

VERIFICATION_USER_NOT_FOUND = (
    "⚠️ <b>User Not Found</b>\n\n"
    "We recognized your hand pattern but couldn't find a matching profile.\n\n"
    "Possible solutions:\n"
    "• Check if you're registered in the system 📝\n"
    "• Contact your administrator for assistance 👨‍💻"
)

VERIFICATION_ERROR = (
    "⚠️ <b>Verification Error</b>\n\n"
    "Oops! Something went wrong during verification.\n\n"
    "Our team has been notified. Please try again later.\n\n"
    "We apologize for the inconvenience! 😔"
)