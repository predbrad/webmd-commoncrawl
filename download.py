from comcrawl import IndexClient
import pandas as pd

client = IndexClient(["2022-33"])
client.search("webmd.com/drugs/*")
client.results = (pd.DataFrame(client.results)
                  .sort_values(by="timestamp")
                  .drop_duplicates("urlkey", keep="last")
                  .to_dict("records"))
client.download()

pd.DataFrame(client.results).to_csv("results.csv")

df = pd.DataFrame(client.results)

print(df.head())





