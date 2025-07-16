chart_providers = [
    {
        "name": "TradingView",
        "type": "iframe",
        "asset_classes": ["stocks", "crypto", "forex", "futures"],
        "default": True,
        "supports_overlay": True,
        "region_safe": True,
        "embed_template": lambda symbol: f"""
            <iframe src="https://s.tradingview.com/widgetembed/?symbol={symbol}&interval=D&theme=dark"
            width="100%" height="600" frameborder="0" allowfullscreen></iframe>
        """
    },
    {
        "name": "Plotly",
        "type": "native",
        "asset_classes": ["all"],
        "default": False,
        "supports_overlay": True,
        "region_safe": True,
        "embed_template": None
    },
    {
        "name": "Investing.com",
        "type": "iframe",
        "asset_classes": ["stocks", "crypto", "forex", "futures"],
        "default": False,
        "supports_overlay": False,
        "region_safe": True,
        "embed_template": lambda symbol: f"""
            <iframe src="https://ssltvc.forexpros.com/?pair_ID=1&symbol={symbol}&interval=86400&theme=dark"
            width="100%" height="600" frameborder="0" allowfullscreen></iframe>
        """
    },
    {
        "name": "Coinalyze",
        "type": "iframe",
        "asset_classes": ["crypto"],
        "default": False,
        "supports_overlay": False,
        "region_safe": True,
        "embed_template": lambda symbol: f"""
            <iframe src="https://coinalyze.net/crypto-charts/binance/{symbol.lower().replace('-', '').replace('usdt', 'usdt-perp')}/"
            width="100%" height="600" frameborder="0" allowfullscreen></iframe>
        """
    },
    {
        "name": "Coinigy",
        "type": "iframe",
        "asset_classes": ["crypto"],
        "default": False,
        "supports_overlay": False,
        "region_safe": True,
        "embed_template": lambda symbol: f"""
            <iframe src="https://www.coinigy.com/s/i/{symbol.replace('-', '')}/"
            width="100%" height="600" frameborder="0" allowfullscreen></iframe>
        """
    },
    {
        "name": "MetaTrader Web",
        "type": "iframe",
        "asset_classes": ["forex"],
        "default": False,
        "supports_overlay": False,
        "region_safe": True,
        "embed_template": lambda symbol: f"""
            <iframe src="https://www.metatraderweb.app/terminal?symbol={symbol}&lang=en"
            width="100%" height="600" frameborder="0" allowfullscreen></iframe>
        """
    },
    {
        "name": "StockCharts",
        "type": "img",
        "asset_classes": ["stocks", "etf"],
        "default": False,
        "supports_overlay": False,
        "region_safe": True,
        "embed_template": lambda symbol: f"""
            <img src="https://stockcharts.com/c-sc/sc?s={symbol}&p=D&b=5&g=0&i=0&r=168" width="100%" />
        """
    },
    {
        "name": "Yahoo Finance",
        "type": "iframe",
        "asset_classes": ["stocks", "crypto"],
        "default": False,
        "supports_overlay": False,
        "region_safe": True,
        "embed_template": lambda symbol: f"""
            <iframe src="https://finance.yahoo.com/chart/{symbol}" width="100%" height="600" frameborder="0" allowfullscreen></iframe>
        """
    }
]
