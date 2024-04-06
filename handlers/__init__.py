from aiogram import Router


def get_handlers_router() -> Router:
    from . import info, start

    router = Router()
    router.include_router(start.router)
    router.include_router(info.router)

    return router
