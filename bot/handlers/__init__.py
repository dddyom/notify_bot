from aiogram import Router


def get_handlers_router() -> Router:
    from . import info

    router = Router()
    router.include_router(info.router)

    return router
