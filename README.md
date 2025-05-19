# IBKR Tools

Small collection of scripts for pulling market data and generating basic technical signals. They can use Interactive Brokers (TWS or Gateway) for live data and fall back to Yahoo Finance when needed.

## Requirements

- **Python** 3.11 or newer
- Install Python dependencies from [requirements.txt](requirements.txt):

```bash
pip install -r requirements.txt
```

## IBKR / TWS Gateway Setup

If you want to use the IBKR powered scripts you must have Trader Workstation or the IB Gateway running locally.

1. Launch TWS or IB Gateway and log in.
2. Open **Configure → API → Settings** and enable *Allow connections from localhost*.
3. Note the port (default `7497` for paper trading). If you use a different host/port/client ID, update the `IB_HOST`, `IB_PORT` and `IB_CID` variables inside the scripts.

## Usage

The utilities read ticker symbols from `tickers_live.txt` (preferred) or `tickers.txt` in the repository root. Edit those files with the symbols you care about.

### `tech_signals_ibkr.py`
Fetch technical indicators via the IBKR API and save a dated CSV.

```bash
python tech_signals_ibkr.py
# → tech_signals_YYYYMMDD.csv
```

### `tech_signals.py`
Same indicators using only Yahoo Finance. Useful when the IB Gateway is not running.

```bash
python tech_signals.py
# → tech_signals.csv
```

### `live_feed.py`
Retrieve the latest quotes for your tickers. IBKR is tried first, then Yahoo Finance. Output file names include a timestamp.

```bash
python live_feed.py
# → live_quotes_YYYYMMDD_HHMM.csv
```

### `historic_prices.py`
Download 60 days of daily OHLCV data for all tickers plus core indices.

```bash
python historic_prices.py
# → historic_prices_YYYYMMDD.csv
```

All resulting CSV files are written to the repository root.
