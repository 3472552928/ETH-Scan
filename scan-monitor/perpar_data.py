# pc端钉钉申请的token
dingding_token = "98bce2d980abdd565efe2b55e3cad2aec65cfd6e16154d40d320c1442eca171b"           # 必填
# ---- 区块浏览器申请的apikey ----
apikey_FTM = ""               #必填
apikey_MATIC = ""             #必填
apikey_BSC = ""               #必填
apikey_ETH = "WQXTJFWCTCGDMSNQYY6YTUAA13HAWVIGWQ"               #必填
apikey_AVAX = ""              #必填

# 填写需要监控的地址
oxdata = {
    "0xd350044e87a7ce167f524f2e137925060f3e190d",
    "0xab4bcdac140c2c5c3351c554b5d188ae6abcfba3"

}

# oxdata = {
#     "0x159780bfe07D5936e8d79EAB1d882025fDBc8B2a",
#      "0xd350044e87a7ce167f524f2e137925060f3e190d",
#       "0xae2fc483527b8ef99eb5d9b44875f005ba1fae13",
# }
#接收方的智能合约地址，方便查阅
contract_list = {
    "0x10ed43c718714eb63d5aa57b78b54704e256024e":"pancake routerV2",
    "0x95c78222b3d6e262426483d42cfa53685a67ab9d":"Venus: vBUSD Token",
    "0x1a1ec25DC08e98e5E93F1104B5e5cdD298707d31":"Metamask: Swap Router",
    "0xe9e7cea3dedca5984780bafc599bd69add087d56":"Binance: BUSD Stablecoin",
    "0x8f8dd7db1bda5ed3da8c9daf3bfa471c12d58486":"Dodoex: V2 Proxy",
    "0x7be8076f4ea4a4ad08075c2508e481d6c946d12b":"Opensea"
}
# 当前transfer的方式
method_data = {
    "0x095ea7b3":"Approve/授权",
    "0xb6f9de95":"Swap Exact ETH For Tokens/买入",
    "0x791ac947":"Swap Exact Token For ETH/卖出",
    "0x":"Transfer/转账",
    "0xf305d719":"Add Liquiity ETH",
    "0xfb3bdb41":"Swap ETH For Exact Tokens",
    "0xa22cb465":"setApprovalForAll",
    "0xab834bab":"atomicMatch_(buy_nft)",
    "0x02751cec":"Remove Liquidity ETH"
}