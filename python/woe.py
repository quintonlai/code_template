def woe(df, x, y):
        woe_temp = pd.crosstab(df[x], df[y])
        woe_temp['sub_total'] = woe_temp[0] + woe_temp[1]
        woe_temp['pct_good'] = woe_temp[0] / woe_temp['sub_total']
        woe_temp['pct_bad'] = woe_temp[1] / woe_temp['sub_total']
        woe_temp['woe'] = np.log(woe_temp['pct_good'] / woe_temp['pct_bad'])
        woe_temp['iv'] = (woe_temp['pct_good'] - woe_temp['pct_bad']) * woe_temp['woe']
        woe_temp = woe_temp[np.isfinite(woe_temp).all(1)]
        return woe_temp
