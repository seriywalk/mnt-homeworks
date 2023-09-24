import sentry_sdk

sentry_sdk.init(
    dsn="https://d726d11e43ac1fec901c31de4d8047bb@o4505934856650752.ingest.sentry.io/4505935337291776",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    # traces_sample_rate=1.0,
    environment="development",
    release="1.1",
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    # profiles_sample_rate=1.0,
)

if __name__ == "__main__":
    division_by_zero = 1 / 0
