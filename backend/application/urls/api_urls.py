from ..apis import userInfoBase, carInfoBase
def init_apis(app):
    app.include_router(userInfoBase.router, prefix="/api", tags=["UserInfoBase"])
    app.include_router(carInfoBase.router, prefix="/api", tags=["CarInfoBase"])