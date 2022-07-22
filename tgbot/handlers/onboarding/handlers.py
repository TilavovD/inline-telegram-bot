from post.models import Post

from telegram import ParseMode, Update, InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.ext import CallbackContext

from tgbot.handlers.onboarding import static_text
from tgbot.models import User
from uuid import uuid4



def command_start(update: Update, context: CallbackContext) -> None:
    u, created = User.get_user_and_created(update, context)

    if created:
        text = static_text.start_created.format(first_name=u.first_name)
    else:
        text = static_text.start_not_created.format(first_name=u.first_name)

    update.message.reply_text(text=text)


def inlinequery(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    query = update.inline_query.query
        
    if query == "":
        return 

    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title=post.title,
            description=post.sub_content,
            input_message_content=InputTextMessageContent(
                f"<b><a href='{post.image}'>{post.title}</a></b>\n\n{post.content}", 
                parse_mode=ParseMode.HTML),
            thumb_url=post.image
         
        ) for post in Post.objects.filter(title__icontains=query)

    ]    
    update.inline_query.answer(results)

    