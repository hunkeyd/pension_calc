#!/usr/bin/env python3

'''This calculator is a general estimate of the worth of a military pension.  It will give a general 
estimate of retired military pay for each grade based on the service members time in service. The
calculator assumes that you'll spend the last three years of service at the same rank.  If you're
promoted in those last three years, you'll recieve a pension somewhere between the two ranks served.
I recommend using this calculator to understand ballpark what a military pension is worth annually.
'''

# https://www.dfas.mil/Portals/98/Documents/militarymembers/militarymembers/pay-tables/2021%20MilPay%20General.pdf?ver=MkfmQyc245XzKP414-iRVA%3d%3d
fy2021 = {'PAYGRADE':[0,2,3,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40], # this first row are the years served
'O10':[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,16608.30,16608.30,16608.30,16608.30,16608.30,16608.30,16608.30,16608.30,16608.30,16608.30,16608.30],
'O9':[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,16012.50,16243.80,16576.80,16608.30,16608.30,16608.30,16608.30,16608.30,16608.30,16608.30,16608.30],
'O8':[11329.50,11701.20,11947.50,12016.20,12323.40,12836.70,12956.40,13443.60,13584.00,14004.00,14611.80,15171.90,15546.00,15546.00,15546.00,15546.00,15935.40,15935.40,16333.20,16333.20,16333.20,16333.20],
'O7':[9414.30,9851.40,10053.90,10215.00,10506.00,10794.00,11126.70,11458.20,11791.20,12836.70,13719.30,13719.30,13719.30,13719.30,13789.80,13789.80,14065.80,14065.80,14065.80,14065.80,14065.80,14065.80],
'O6':[7139.10,7842.90,8357.70,8357.70,8389.80,8749.20,8796.90,8796.90,9296.70,10180.50,10699.20,11217.60,11512.80,11811.90,12390.90,12390.90,12638.40,12638.40,12638.40,12638.40,12638.40,12638.40],
'O5':[5951.40,6704.40,7168.20,7255.50,7545.60,7718.40,8099.40,8379.60,8740.80,9293.10,9555.90,9816.00,10111.20,10111.20,10111.20,10111.20,10111.20,10111.20,10111.20,10111.20,10111.20,10111.20],
'O4':[5135.10,5943.90,6341.10,6429.00,6797.10,7192.20,7684.20,8066.70,8332.50,8485.50,8573.70,8573.70,8573.70,8573.70,8573.70,8573.70,8573.70,8573.70,8573.70,8573.70,8573.70,8573.70],
'O3':[4514.70,5117.70,5523.30,6022.80,6311.70,6628.20,6832.80,7169.40,7345.20,7345.20,7345.20,7345.20,7345.20,7345.20,7345.20,7345.20,7345.20,7345.20,7345.20,7345.20,7345.20,7345.20],
'O2':[3901.20,4442.70,5116.80,5289.90,5398.50,5398.50,5398.50,5398.50,5398.50,5398.50,5398.50,5398.50,5398.50,5398.50,5398.50,5398.50,5398.50,5398.50,5398.50,5398.50,5398.50,5398.50],
'O1':[3385.80,3524.40,4260.60,4260.60,4260.60,4260.60,4260.60,4260.60,4260.60,4260.60,4260.60,4260.60,4260.60,4260.60,4260.60,4260.60,4260.60,4260.60,4260.60,4260.60,4260.60,4260.60],
'O3E':[0.00,0.00,0.00,6022.80,6311.70,6628.20,6832.80,7169.40,7453.50,7617.00,7839.00,7839.00,7839.00,7839.00,7839.00,7839.00,7839.00,7839.00,7839.00,7839.00,7839.00,7839.00],
'O2E':[0.00,0.00,0.00,5289.90,5398.50,5570.40,5860.50,6084.90,6251.70,6251.70,6251.70,6251.70,6251.70,6251.70,6251.70,6251.70,6251.70,6251.70,6251.70,6251.70,6251.70,6251.70],
'O1E':[0.00,0.00,0.00,4260.60,4549.50,4717.50,4889.70,5058.30,5289.90,5289.90,5289.90,5289.90,5289.90,5289.90,5289.90,5289.90,5289.90,5289.90,5289.90,5289.90,5289.90,5289.90],
'W5':[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,8296.20,8716.80,9030.60,9377.10,9377.10,9846.90,9846.90,10338.60,10338.60,10856.40,10856.40],
'W4':[4665.90,5018.70,5162.70,5304.60,5548.80,5790.30,6035.10,6402.60,6725.10,7032.00,7283.40,7528.50,7888.20,8183.70,8520.90,8520.90,8691.00,8691.00,8691.00,8691.00,8691.00,8691.00],
'W3':[4261.20,4438.50,4620.90,4680.30,4870.80,5246.40,5637.30,5821.50,6034.80,6253.80,6648.90,6915.00,7074.30,7243.50,7474.50,7474.50,7474.50,7474.50,7474.50,7474.50,7474.50,7474.50],
'W2':[3770.40,4127.10,4236.60,4312.20,4556.40,4936.50,5125.20,5310.30,5537.10,5714.40,5874.60,6066.90,6193.20,6293.10,6293.10,6293.10,6293.10,6293.10,6293.10,6293.10,6293.10,6293.10],
'W1':[3309.30,3666.00,3761.40,3963.90,4203.00,4555.80,4720.20,4950.90,5177.40,5355.60,5519.40,5718.60,5718.60,5718.60,5718.60,5718.60,5718.60,5718.60,5718.60,5718.60,5718.60,5718.60],
'E9':[0.00,0.00,0.00,0.00,0.00,0.00,5637.00,5764.80,5925.90,6114.90,6306.60,6612.00,6871.50,7143.30,7560.30,7560.30,7937.70,7937.70,8334.90,8334.90,8752.50,8752.50],
'E8':[0.00,0.00,0.00,0.00,0.00,4614.60,4818.60,4944.90,5096.10,5260.50,5556.30,5706.30,5961.60,6103.50,6451.80,6451.80,6581.40,6581.40,6581.40,6581.40,6581.40,6581.40],
'E7':[3207.60,3501.00,3635.40,3812.40,3951.30,4189.50,4323.90,4561.80,4760.10,4895.10,5039.10,5094.90,5282.40,5382.90,5765.40,5765.40,5765.40,5765.40,5765.40,5765.40,5765.40,5765.40],
'E6':[2774.40,3053.10,3188.10,3318.90,3455.40,3762.60,3882.90,4114.50,4185.30,4236.90,4297.20,4297.20,4297.20,4297.20,4297.20,4297.20,4297.20,4297.20,4297.20,4297.20,4297.20,4297.20],
'E5':[2541.60,2712.90,2844.00,2978.10,3187.20,3405.60,3585.30,3606.90,3606.90,3606.90,3606.90,3606.90,3606.90,3606.90,3606.90,3606.90,3606.90,3606.90,3606.90,3606.90,3606.90,3606.90],
'E4':[2330.40,2449.80,2582.40,2713.50,2829.00,2829.00,2829.00,2829.00,2829.00,2829.00,2829.00,2829.00,2829.00,2829.00,2829.00,2829.00,2829.00,2829.00,2829.00,2829.00,2829.00,2829.00],
'E3':[2103.90,2236.20,2371.80,2371.80,2371.80,2371.80,2371.80,2371.80,2371.80,2371.80,2371.80,2371.80,2371.80,2371.80,2371.80,2371.80,2371.80,2371.80,2371.80,2371.80,2371.80,2371.80],
'E2':[2000.70,2000.70,2000.70,2000.70,2000.70,2000.70,2000.70,2000.70,2000.70,2000.70,2000.70,2000.70,2000.70,2000.70,2000.70,2000.70,2000.70,2000.70,2000.70,2000.70,2000.70,2000.70],
'E1':[1785.00,1785.00,1785.00,1785.00,1785.00,1785.00,1785.00,1785.00,1785.00,1785.00,1785.00,1785.00,1785.00,1785.00,1785.00,1785.00,1785.00,1785.00,1785.00,1785.00,1785.00,1785.00]}

#https://www.dfas.mil/Portals/98/2020%20Military%20Pay_Basic_DP.pdf
fy2020 = {'PAYGRADE':[0,2,3,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40],
'O10':[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,16441.80,16441.80,16441.80,16441.80,16441.80,16441.80,16441.80,16441.80,16441.80,16441.80,16441.80],
'O9':[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,15546.00,15770.70,16094.10,16441.80,16441.80,16441.80,16441.80,16441.80,16441.80,16441.80,16441.80],
'O8':[10999.50,11360.40,11599.50,11666.10,11964.60,12462.90,12579.00,13052.10,13188.30,13596.00,14186.10,14730.00,15093.30,15093.30,15093.30,15093.30,15471.30,15471.30,15857.40,15857.40,15857.40,15857.40],
'O7':[9140.10,9564.60,9761.10,9917.40,10200.00,10479.60,10802.70,11124.60,11447.70,12462.90,13319.70,13319.70,13319.70,13319.70,13388.10,13388.10,13656.00,13656.00,13656.00,13656.00,13656.00,13656.00],
'O6':[6931.20,7614.60,8114.40,8114.40,8145.30,8494.50,8540.70,8540.70,9025.80,9884.10,10387.50,10890.90,11177.40,11467.80,12030.00,12030.00,12270.30,12270.30,12270.30,12270.30,12270.30,12270.30],
'O5':[5778.00,6509.10,6959.40,7044.30,7325.70,7493.70,7863.60,8135.40,8486.10,9022.50,9277.50,9530.10,9816.60,9816.60,9816.60,9816.60,9816.60,9816.60,9816.60,9816.60,9816.60,9816.60],
'O4':[4985.40,5770.80,6156.30,6241.80,6599.10,6982.80,7460.40,7831.80,8089.80,8238.30,8324.10,8324.10,8324.10,8324.10,8324.10,8324.10,8324.10,8324.10,8324.10,8324.10,8324.10,8324.10],
'O3':[4383.30,4968.60,5362.50,5847.30,6127.80,6435.00,6633.90,6960.60,7131.30,7131.30,7131.30,7131.30,7131.30,7131.30,7131.30,7131.30,7131.30,7131.30,7131.30,7131.30,7131.30,7131.30],
'O2':[3787.50,4313.40,4967.70,5135.70,5241.30,5241.30,5241.30,5241.30,5241.30,5241.30,5241.30,5241.30,5241.30,5241.30,5241.30,5241.30,5241.30,5241.30,5241.30,5241.30,5241.30,5241.30],
'O1':[3287.10,3421.80,4136.40,4136.40,4136.40,4136.40,4136.40,4136.40,4136.40,4136.40,4136.40,4136.40,4136.40,4136.40,4136.40,4136.40,4136.40,4136.40,4136.40,4136.40,4136.40,4136.40],
'O3E':[0.00,0.00,0.00,5847.30,6127.80,6435.00,6633.90,6960.60,7236.30,7395.00,7610.70,7610.70,7610.70,7610.70,7610.70,7610.70,7610.70,7610.70,7610.70,7610.70,7610.70,7610.70],
'O2E':[0.00,0.00,0.00,5135.70,5241.30,5408.10,5689.80,5907.60,6069.60,6069.60,6069.60,6069.60,6069.60,6069.60,6069.60,6069.60,6069.60,6069.60,6069.60,6069.60,6069.60,6069.60],
'O1E':[0.00,0.00,0.00,4136.40,4416.90,4580.10,4747.20,4911.00,5135.70,5135.70,5135.70,5135.70,5135.70,5135.70,5135.70,5135.70,5135.70,5135.70,5135.70,5135.70,5135.70,5135.70],
'W5':[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00, 8054.70,8463.00,8767.50,9104.10,9104.10,9560.10,9560.10,10037.40,10037.40,10540.20,10540.20],
'W4':[4530.00,4872.60,5012.40,5150.10,5387.10,5621.70,5859.30,6216.00,6529.20,6827.10,7071.30,7309.20,7658.40,7945.20,8272.80,8272.80,8437.80,8437.80,8437.80,8437.80,8437.80,8437.80],
'W3':[4137.00,4309.20,4486.20,4544.10,4728.90,5093.70,5473.20,5652.00,5859.00,6071.70,6455.10,6713.70,6868.20,7032.60,7256.70,7256.70,7256.70,7256.70,7256.70,7256.70,7256.70,7256.70],
'W2':[3660.60,4006.80,4113.30,4186.50,4423.80,4792.80,4975.80,5155.50,5375.70,5547.90,5703.60,5890.20,6012.90,6109.80,6109.80,6109.80,6109.80,6109.80,6109.80,6109.80,6109.80,6109.80],
'W1':[3213.00,3559.20,3651.90,3848.40,4080.60,4423.20,4582.80,4806.60,5026.50,5199.60,5358.60,5552.10,5552.10,5552.10,5552.10,5552.10,5552.10,5552.10,5552.10,5552.10,5552.10,5552.10],
'E9':[0.00,0.00,0.00,0.00,0.00,0.00,5472.90,5596.80,5753.40,5936.70,6123.00,6419.40,6671.40,6935.10,7340.10,7340.10,7706.40,7706.40,8092.20,8092.20,8497.50,8497.50],
'E8':[0.00,0.00,0.00,0.00,0.00,4480.20,4678.20,4800.90,4947.60,5107.20,5394.60,5540.10,5787.90,5925.60,6264.00,6264.00,6389.70,6389.70,6389.70,6389.70,6389.70,6389.70],
'E7':[3114.30,3399.00,3529.50,3701.40,3836.10,4067.40,4197.90,4428.90,4621.50,4752.60,4892.40,4946.40,5128.50,5226.00,5597.40,5597.40,5597.40,5597.40,5597.40,5597.40,5597.40,5597.40],
'E6':[2693.70,2964.30,3095.10,3222.30,3354.90,3653.10,3769.80,3994.80,4063.50,4113.60,4172.10,4172.10,4172.10,4172.10,4172.10,4172.10,4172.10,4172.10,4172.10,4172.10,4172.10,4172.10],
'E5':[2467.50,2634.00,2761.20,2891.40,3094.50,3306.30,3480.90,3501.90,3501.90,3501.90,3501.90,3501.90,3501.90,3501.90,3501.90,3501.90,3501.90,3501.90,3501.90,3501.90,3501.90,3501.90],
'E4':[2262.60,2378.40,2507.10,2634.60,2746.50,2746.50,2746.50,2746.50,2746.50,2746.50,2746.50,2746.50,2746.50,2746.50,2746.50,2746.50,2746.50,2746.50,2746.50,2746.50,2746.50,2746.50],
'E3':[2042.70,2171.10,2302.80,2302.80,2302.80,2302.80,2302.80,2302.80,2302.80,2302.80,2302.80,2302.80,2302.80,2302.80,2302.80,2302.80,2302.80,2302.80,2302.80,2302.80,2302.80,2302.80],
'E2':[1942.50,1942.50,1942.50,1942.50,1942.50,1942.50,1942.50,1942.50,1942.50,1942.50,1942.50,1942.50,1942.50,1942.50,1942.50,1942.50,1942.50,1942.50,1942.50,1942.50,1942.50,1942.50],
'E1':[1733.10,1733.10,1733.10,1733.10,1733.10,1733.10,1733.10,1733.10,1733.10,1733.10,1733.10,1733.10,1733.10,1733.10,1733.10,1733.10,1733.10,1733.10,1733.10,1733.10,1733.10,1733.10]}

#https://www.dfas.mil/Portals/98/MilPayTable2019_3.pdf
fy2019 = {'PAYGRADE':[0,2,3,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40],
'O10':[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,16025.10,16025.10,16025.10,16025.10,16025.10,16025.10,16025.10,16025.10,16025.10,16025.10,16025.10],
'O9':[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,15078.60,15296.40,15610.20,16025.10,16025.10,16025.10,16025.10,16025.10,16025.10,16025.10,16025.10],
'O8':[10668.90,11018.70,11250.60,11315.40,11604.90,12088.20,12200.70,12659.70,12791.70,13187.10,13759.50,14287.20,14639.40,14639.40,14639.40,14639.40,15006.00,15006.00,15380.70,15380.70,15380.70,15380.70],
'O7':[8865.30,9276.90,9467.70,9619.20,9893.40,10164.60,10477.80,10790.10,11103.60,12088.20,12919.20,12919.20,12919.20,12919.20,12985.50,12985.50,13245.30,13245.30,13245.30,13245.30,13245.30,13245.30],
'O6':[6722.70,7385.70,7870.50,7870.50,7900.50,8239.20,8283.90,8283.90,8754.30,9586.80,10075.20,10563.30,10841.40,11123.10,11668.20,11668.20,11901.30,11901.30,11901.30,11901.30,11901.30,11901.30],
'O5':[5604.30,6313.50,6750.00,6832.50,7105.50,7268.40,7627.20,7890.90,8230.80,8751.30,8998.50,9243.60,9521.40,9521.40,9521.40,9521.40,9521.40,9521.40,9521.40,9521.40,9521.40,9521.40],
'O4':[4835.40,5597.40,5971.20,6054.00,6400.80,6772.80,7236.00,7596.30,7846.50,7990.50,8073.90,8073.90,8073.90,8073.90,8073.90,8073.90,8073.90,8073.90,8073.90,8073.90,8073.90,8073.90],
'O3':[4251.60,4819.20,5201.40,5671.50,5943.60,6241.50,6434.40,6751.20,6916.80,6916.80,6916.80,6916.80,6916.80,6916.80,6916.80,6916.80,6916.80,6916.80,6916.80,6916.80,6916.80,6916.80],
'O2':[3673.50,4183.80,4818.30,4981.20,5083.80,5083.80,5083.80,5083.80,5083.80,5083.80,5083.80,5083.80,5083.80,5083.80,5083.80,5083.80,5083.80,5083.80,5083.80,5083.80,5083.80,5083.80],
'O1':[3188.40,3318.90,4011.90,4011.90,4011.90,4011.90,4011.90,4011.90,4011.90,4011.90,4011.90,4011.90,4011.90,4011.90,4011.90,4011.90,4011.90,4011.90,4011.90,4011.90,4011.90,4011.90],
'O3E':[0.00,0.00,0.00,5671.50,5943.60,6241.50,6434.40,6751.20,7018.80,7172.70,7381.80,7381.80,7381.80,7381.80,7381.80,7381.80,7381.80,7381.80,7381.80,7381.80,7381.80,7381.80],
'O2E':[0.00,0.00,0.00,4981.20,5083.80,5245.50,5518.80,5730.00,5887.20,5887.20,5887.20,5887.20,5887.20,5887.20,5887.20,5887.20,5887.20,5887.20,5887.20,5887.20,5887.20,5887.20],
'O1E':[0.00,0.00,0.00,4011.90,4284.00,4442.40,4604.40,4763.40,4981.20,4981.20,4981.20,4981.20,4981.20,4981.20,4981.20,4981.20,4981.20,4981.20,4981.20,4981.20,4981.20,4981.20],
'W5':[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,7812.60,8208.60,8503.80,8830.50,8830.50,9272.70,9272.70,9735.60,9735.60,10223.40,10223.4],
'W4':[4393.80,4726.20,4861.80,4995.30,5225.10,5452.80,5683.20,6029.10,6333.00,6621.90,6858.60,7089.30,7428.00,7706.40,8024.10,8024.10,8184.00,8184.00,8184.00,8184.00,8184.00,8184.00],
'W3':[4012.50,4179.60,4351.20,4407.60,4586.70,4940.40,5308.50,5482.20,5682.90,5889.00,6261.00,6511.80,6661.80,6821.10,7038.60,7038.60,7038.60,7038.60,7038.60,7038.60,7038.60,7038.60],
'W2':[3550.50,3886.20,3989.70,4060.50,4290.90,4648.80,4826.10,5000.40,5214.00,5381.10,5532.00,5713.20,5832.00,5926.20,5926.20,5926.20,5926.20,5926.20,5926.20,5926.20,5926.20,5926.20],
'W1':[3116.40,3452.10,3542.10,3732.60,3957.90,4290.30,4445.10,4662.00,4875.30,5043.30,5197.50,5385.30,5385.30,5385.30,5385.30,5385.30,5385.30,5385.30,5385.30,5385.30,5385.30,5385.30],
'E9':[0.00,0.00,0.00,0.00,0.00,0.00,5308.20,5428.50,5580.30,5758.20,5938.80,6226.50,6470.70,6726.60,7119.30,7119.30,7474.80,7474.80,7848.90,7848.90,8241.90,8241.90],
'E8':[0.00,0.00,0.00,0.00,0.00,4345.50,4537.50,4656.60,4798.80,4953.60,5232.30,5373.60,5613.90,5747.40,6075.60,6075.60,6197.70,6197.70,6197.70,6197.70,6197.70,6197.70],
'E7':[3020.70,3296.70,3423.30,3590.10,3720.90,3945.00,4071.60,4295.70,4482.60,4609.80,4745.40,4797.60,4974.30,5068.80,5429.10,5429.10,5429.10,5429.10,5429.10,5429.10,5429.10,5429.10],
'E6':[2612.70,2875.20,3002.10,3125.40,3254.10,3543.30,3656.40,3874.80,3941.40,3990.00,4046.70,4046.70,4046.70,4046.70,4046.70,4046.70,4046.70,4046.70,4046.70,4046.70,4046.70,4046.70],
'E5':[2393.40,2554.80,2678.10,2804.40,3001.50,3207.00,3376.20,3396.60,3396.60,3396.60,3396.60,3396.60,3396.60,3396.60,3396.60,3396.60,3396.60,3396.60,3396.60,3396.60,3396.60,3396.60],
'E4':[2194.50,2307.00,2431.80,2555.40,2664.00,2664.00,2664.00,2664.00,2664.00,2664.00,2664.00,2664.00,2664.00,2664.00,2664.00,2664.00,2664.00,2664.00,2664.00,2664.00,2664.00,2664.00],
'E3':[1981.20,2105.70,2233.50,2233.50,2233.50,2233.50,2233.50,2233.50,2233.50,2233.50,2233.50,2233.50,2233.50,2233.50,2233.50,2233.50,2233.50,2233.50,2233.50,2233.50,2233.50,2233.50],
'E2':[1884.00,1884.00,1884.00,1884.00,1884.00,1884.00,1884.00,1884.00,1884.00,1884.00,1884.00,1884.00,1884.00,1884.00,1884.00,1884.00,1884.00,1884.00,1884.00,1884.00,1884.00,1884.00],
'E1':[1680.90,1680.90,1680.90,1680.90,1680.90,1680.90,1680.90,1680.90,1680.90,1680.90,1680.90,1680.90,1680.90,1680.90,1680.90,1680.90,1680.90,1680.90,1680.90,1680.90,1680.90,1680.90]}

#https://www.dfas.mil/Portals/98/MilPayTable2018_5.pdf
fy2018 = {'PAYGRADE':[0,2,3,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40],
'O10':[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,115800.10,15800.10,15800.10,15800.10,15800.10,15800.10,15800.10,15800.10,15800.10,15800.10,15800.10],
'O9':[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,114696.40,14908.80,15214.50,15747.60,15747.60,15800.10,15800.10,15800.10,15800.10,15800.10,15800.10],
'O8':[110398.60,10739.40,10965.60,11028.60,11310.90,11781.90,11891.40,12339.00,12467.40,12852.90,13410.90,13925.10,14268.30,14268.30,14268.30,14268.30,14625.60,14625.60,14991.00,14991.00,14991.00,14991.00],
'O7':[18640.60,9041.70,9227.70,9375.30,9642.60,9906.90,10212.30,10516.80,10822.20,11781.90,12591.90,12591.90,12591.90,12591.90,12656.40,12656.40,12909.60,12909.60,12909.60,12909.60,12909.60,12909.60],
'O6':[26552.30,7198.50,7671.00,7671.00,7700.40,8030.40,8073.90,8073.90,8532.60,9343.80,9819.90,10295.70,10566.60,10841.10,11372.40,11372.40,11599.80,11599.80,11599.80,11599.80,11599.80,11599.80],
'O5':[5462.40,6153.60,6579.00,6659.40,6925.50,7084.20,7434.00,7690.80,8022.30,8529.60,8770.50,9009.30,9280.20,9280.20,9280.20,9280.20,9280.20,9280.20,9280.20,9280.20,9280.20,9280.20],
'O4':[4713.00,5455.50,5820.00,5900.70,6238.50,6601.20,7052.70,7403.70,7647.60,7788.00,7869.30,7869.30,7869.30,7869.30,7869.30,7869.30,7869.30,7869.30,7869.30,7869.30,7869.30,7869.30],
'O3':[4143.90,4697.10,5069.70,5527.80,5793.00,6083.40,6271.20,6580.20,6741.60,6741.60,6741.60,6741.60,6741.60,6741.60,6741.60,6741.60,6741.60,6741.60,6741.60,6741.60,6741.60,6741.60],
'O2':[3580.50,4077.90,4696.20,4854.90,4955.10,4955.10,4955.10,4955.10,4955.10,4955.10,4955.10,4955.10,4955.10,4955.10,4955.10,4955.10,4955.10,4955.10,4955.10,4955.10,4955.10,4955.10],
'O1':[3107.70,3234.90,3910.20,3910.20,3910.20,3910.20,3910.20,3910.20,3910.20,3910.20,3910.20,3910.20,3910.20,3910.20,3910.20,3910.20,3910.20,3910.20,3910.20,3910.20,3910.20,3910.20],
'O3E':[0.00,0.00,0.00,5527.80,5793.00,6083.40,6271.20,6580.20,6840.90,6990.90,7194.60,7194.60,7194.60,7194.60,7194.60,7194.60,7194.60,7194.60,7194.60,7194.60,7194.60,7194.60],
'O2E':[0.00,0.00,0.00,4854.90,4955.10,5112.60,5379.00,5584.80,5738.10,5738.10,5738.10,5738.10,5738.10,5738.10,5738.10,5738.10,5738.10,5738.10,5738.10,5738.10,5738.10,5738.10],
'O1E':[0.00,0.00,0.00,3910.20,4175.40,4329.90,4487.70,4642.80,4854.90,4854.90,4854.90,4854.90,4854.90,4854.90,4854.90,4854.90,4854.90,4854.90,4854.90,4854.90,4854.90,4854.90], 
'W5':[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,7614.60,8000.70,8288.40,8606.70,8606.70,9037.80,9037.80,9489.00,9489.00,9964.20,9964.20],
'W4':[4282.50,4606.50,4738.50,4868.70,5092.80,5314.50,5539.20,5876.40,6172.50,6454.20,6684.90,6909.60,7239.90,7511.10,7820.70,7820.70,7976.70,7976.70,7976.70,7976.70,7976.70,7976.70],
'W3':[3910.80,4073.70,4240.80,4296.00,4470.60,4815.30,5174.10,5343.30,5538.90,5739.90,6102.30,6346.80,6492.90,6648.30,6860.10,6860.10,6860.10,6860.10,6860.10,6860.10,6860.10,6860.10],
'W2':[3460.50,3787.80,3888.60,3957.60,4182.30,4530.90,4703.70,4873.80,5082.00,5244.60,5391.90,5568.30,5684.10,5775.90,5775.90,5775.90,5775.90,5775.90,5775.90,5775.90,5775.90,5775.90],
'W1':[3037.50,3364.50,3452.40,3638.10,3857.70,4181.70,4332.60,4543.80,4751.70,4915.50,5065.80,5248.80,5248.80,5248.80,5248.80,5248.80,5248.80,5248.80,5248.80,5248.80,5248.80,5248.80],
'E9':[0.00,0.00,0.00,0.00,0.00,0.00,5173.80,5290.80,5439.00,5612.40,5788.20,6068.70,6306.60,6556.20,6939.00,6939.00,7285.50,7285.50,7650.00,7650.00,8033.10,8033.10],
'E8':[0.00,0.00,0.00,0.00,0.00,4235.40,4422.60,4538.70,4677.30,4828.20,5099.70,5237.40,5471.70,5601.90,5921.70,5921.70,6040.50,6040.50,6040.50,6040.50,6040.50,6040.50],
'E7':[2944.20,3213.30,3336.60,3499.20,3626.70,3845.10,3968.40,4186.80,4368.90,4493.10,4625.10,4676.10,4848.30,4940.40,5291.40,5291.40,5291.40,5291.40,5291.40,5291.40,5291.40,5291.40],
'E6':[2546.40,2802.30,2925.90,3046.20,3171.60,3453.60,3563.70,3776.70,3841.50,3888.90,3944.10,3944.10,3944.10,3944.10,3944.10,3944.10,3944.10,3944.10,3944.10,3944.10,3944.10,3944.10],
'E5':[2332.80,2490.00,2610.30,2733.30,2925.30,3125.70,3290.70,3310.50,3310.50,3310.50,3310.50,3310.50,3310.50,3310.50,3310.50,3310.50,3310.50,3310.50,3310.50,3310.50,3310.50,3310.50],
'E4':[2139.00,2248.50,2370.30,2490.60,2596.50,2596.50,2596.50,2596.50,2596.50,2596.50,2596.50,2596.50,2596.50,2596.50,2596.50,2596.50,2596.50,2596.50,2596.50,2596.50,2596.50,2596.50],
'E3':[1931.10,2052.30,2176.80,2176.80,2176.80,2176.80,2176.80,2176.80,2176.80,2176.80,2176.80,2176.80,2176.80,2176.80,2176.80,2176.80,2176.80,2176.80,2176.80,2176.80,2176.80,2176.80],
'E2':[1836.30,1836.30,1836.30,1836.30,1836.30,1836.30,1836.30,1836.30,1836.30,1836.30,1836.30,1836.30,1836.30,1836.30,1836.30,1836.30,1836.30,1836.30,1836.30,1836.30,1836.30,1836.30],
'E1':[1638.30,1638.30,1638.30,1638.30,1638.30,1638.30,1638.30,1638.30,1638.30,1638.30,1638.30,1638.30,1638.30,1638.30,1638.30,1638.30,1638.30,1638.30,1638.30,1638.30,1638.30,1638.30]}


base_pays = [fy2021, fy2020, fy2019, fy2018]


def validate_rpm(years, months, days):
    '''validates that years, months, and days are within expected bounds'''
    if 0 > years >= 40: # end of paychart
       raise ValueError(f"years must be 0-40, not '{years}'")
    if 0 > months >= 11: # 12 months is a year, lol
       raise ValueError(f"months must be 0-11, not '{months}'")
    if 0 > days >= 31:  # anything over 29 days is counted as a month
        raise ValueError(f"days must be 0-31, not '{days}'")


def rpm(years, months=0, days=0, mult=.025):
    '''Retirement Pay Multiplier is calculated as 2.5 percent for each year served on active duty. 
        Each month is added fractionally to the year, rounded at two decimal places.
            i.e., 8 months divided by 12 = .67
        If days total 29 or more, it counts as a full month, any other days are discarded.
            i.e., 28 days: ignored; 29 days, = 1 month.
        Multiply this figure by 2.5 percent (.025) to determine the RPM:  23.67 X .025 = .59175(rounded to 4 decimal places) = .5918
        If member is under BRS, multiply by 2 percent (adjust multi as necessary).
        https://www.marines.mil/portals/1/Publications/MCO%201900.16%20CH%202.pdf?ver=2019-02-26-080015-447    
        '''
            
    validate_rpm(years, months, days)
    
    months += 1 if days >= 29 else 0  # add a month if days greater than 29
    fraction = [round(x/12, 2) for x in range(0,13)][months] # calculate fractional month of year
    return round((years + fraction) * mult , 4) # rounded to 4 decimal points


def pay_lookup(rank, years, fy):
    ''' return the base pay for the rank and years served. '''
    validate_rpm(years, 0, 0)
    
    if years not in fy['PAYGRADE']:
        years -= 1  # decrement one year to find pay group (13 year Gy paid as 12 year Gy)
    
    index = fy['PAYGRADE'].index(years) # get the column number of the associated year
    return fy[rank][index] #return the rank lookup by column number


def high_3(rank, years, months, days):
    '''calculate average of last 36 months of pay for a single rank'''
    pays = []
    base_pays = [fy2018, fy2019, fy2020, fy2021]
    fy = base_pays.pop() # work with the last fy
    mo = (years * 12) + months + (1 if days >= 29 else 0) # calculate the total number of months served
    for x in range(mo, 0, -1)[:36]:   # working backwards from month 36 (and only using the last 36 months)
        if x % 12 == 0:  # if the year changed, then
            years -= 1   # subtract from year for lookup
            fy = base_pays.pop() # go to next fy
        pay = pay_lookup(rank, years, fy)   # lookup
        pays.append(pay)   # save value
    average = round(sum(pays)/len(pays), 2)
    return average, pays


def retire_pension(rank, years=0, months=0, days=0, mult=.025):
    '''return a monthly payment from the retired pay multiplier and high 36 months'''
    ratio = rpm(years, months, days, mult=mult)
    high_3_pay, all_pays = high_3(rank, years, months, days)
    monthly_retire_pay = high_3_pay * ratio
    return monthly_retire_pay, ratio, all_pays


def annual_salary(rank, years, months=0, days=0, mult=.025):
    '''return an annual pension salary'''
    monthly, ratio, pays = retire_pension(rank, years, months, days, mult)
    return(round(monthly*12, 2))


def print_chart(ranks, years, mult=.025):
    '''pretty print out a rank / years pension pay chart'''
    
    # get salaries
    chart = []
    for r in ranks:
        row = [r]
        for y in years:
            row.append(annual_salary(r, y, mult=mult))
        chart.append(row)
    
    # print it
    print('Rank  ', end='')
    for y in years:
        print(f"{y} years   ", end='')
    print('\n', '-'*69, sep='')
    for rank in chart:
        for pay in rank:
            if not isinstance(pay, str):
                pay = f' {pay:,.2f}'
                pay = ' '*(11-len(pay)) + pay
            else:
                pay = pay + ' ' * (3 - len(pay))
            print(pay, end='')
        print()
    print()


if __name__ == '__main__':
    ranks = [x for x in fy2021 if x not in ['E1','E2','E3','O6','O7','O8','O9','O10','PAYGRADE']]
    
    print('\nNon-BRS Service Members')
    print_chart(ranks, range(15,21), mult=.025)
    print_chart(ranks, range(20,26), mult=.025)
    print_chart(ranks, range(25,31), mult=.025)
    
    print('\nBRS Service Members')
    print_chart(ranks, range(15,21), mult=.02)
    print_chart(ranks, range(20,26), mult=.02)
    print_chart(ranks, range(25,31), mult=.02)