from ..apis import userInfoBase
def init_apis(app):
    app.include_router(userInfoBase.router, prefix="/api", tags=["UserInfoBase"])