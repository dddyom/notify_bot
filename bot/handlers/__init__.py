from aiogram import Router


def get_handlers_router() -> Router:
    from . import info, message

    router = Router()
    router.include_router(info.router)
    router.include_router(message.router)

    return router
