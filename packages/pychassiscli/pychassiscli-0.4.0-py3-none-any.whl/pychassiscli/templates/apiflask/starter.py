from app import create_app

app = create_app()


if __name__ == "__main__":
    app.logger.warning(
        """
        ----------------------------
        |  app.run() => apiflask run  |
        ----------------------------
        """
    )
    app.run()
