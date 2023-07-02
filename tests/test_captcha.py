import unittest

from captcha import decode_captcha


class TestCaptcha(unittest.TestCase):
    test_captchas = {
        "KBDARB": "data:image/jpeg;base64,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",
        "EWEUPN": "data:image/jpeg;base64,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",
        "LTSLMX": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABGANIDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDyipXt5I4Ip2XEcpIQ5646/wA6dOlssFu0E7ySMhMytHtCNk8A554xUOSQBk4HQV3JuWqOXYtHTbhbFrw+V5S7c/vV3fNnHy5z2NVo1V5VV3Eak4LEE49+KmktGt5JYrhxFKighCM7s4OOPY1GYZFKB1Kb13KX4BHrURldO79P66jaL81pZ3C3txb3dvBHBtEcDl98vYlePx5x1qhNPJcOHlILBQowAOB06U1CodS67lB5GcZFT6jNaz6jcS2Vube2dyY4S27YvpmlCLjLld356abad9dwburjWjtRYxuszm6LkPEY8Kq4GCGzyevGKdp8VnLeIl/cSW9uc7pI495HHHGR3qWyismjuVvWmSZoh9lK4Clyw+9n+HGai1GzOnajcWbTRTGFyhkibKtjuDS5lJuldp66/wCWltLjtbUelrbC3llnuGTKn7OFQN5jAgYbn5eDnvVOtXQ7htNu/wC02sra6hhypjuhlGJGMY7nv+FV7prM2sX2f5p5CXl+QqIzk/IvJyMYOaUaklUcXqu/6eVl33vp2BpWuUqVVLNtVSSegAqYXCrszbwnapU5B+bPc89an0q4u7S8a5sbv7LPDGziTdg4xyB7mtJykotpff8A0xJK4/SbrTbU3X9o2DXYeBkhAkKeW56Nx1rOq3Y2Vxq1+tvCyGeTJzLIqA9zksQKnvdSWfS7PTvsNrE9oX3XES/PLk/xHvis7qNW0dW7X12VnZ29VbTce8dRLtdIGkWRtHujqBLfahIB5Y5+Xb3rOoorWEORWu3vv5/1oS3cKv6NqQ0jVIr1rO3uwgI8qdcqcjHSo4xYf2XcGRpvt/mJ5IUDYUwd2ffpVSpko1YypyWm3roNXi00XboTzKWZoDHCoIWNlwoY9Bjk4J/CqVFKQVYhgQR1BqoR5VYTdy/Z6Ne3thdX8UJNpZ7ftEgIygJ7AkZqTXZdLku4k0mILbxRKhk2splbuxBY4/CltpIb+W5k1K+mtkeMANFDuV3UAKGAIwMUmuTQm6S0tmgltrRTDFcRRbPOAJO5vU81yRc5YhKXS+iuktFu9pO+22j20NHZQ0/r/Iy6fFGshfMiJtUsN38WOw96v2GjSahp15eR3Vsn2YoPJkkw8hY4G0d6kuPDWrWs15FNaFXs08yb5hwu4Lkc88ntW0sTR5nBzSa/4H+a+8nkla9jJqVTCqsCjOxX5TnG1v60ttbm4ukg3pGzHG6Q4A+tXdIn0+3+1NqNgbtXgZYf3pTZJxhvfHpV1Z8sXZNtdF/S/MUVdmZRRRWpIUUVLDAZ9+JIk2ru/eOFz7DPU0m0ldjLR0i/bRjrJiJshL5JlLjO7HTGc1UleRxH5km/agVec7R6U3zH8vy97eXndtzxn1xWx4V0T+39fgsXEwhbJkkiTdsGOCfbOB+Nc9Sp7CnKrWatG722X+f59ikuZqMepQvYrGIQfYrqWctEDL5kWzY/dRycj3qqFZs7QTgZOB0FdBrFtN4R8Rajp0aQTKU8tWnhV/kYAgjPQ+4rPivp9NUPp09xALiDy5z0D5PzAe3Spo1nOkpU/eTSab6311stByjZ2ehPZx6n4p1G1spLsuYoiqPO3yxRqMn8ABWUYm8x1T94Fz8yAkEev0rrPDWg+HtR0z7TqHiH+zroOyGIsoyuOoz2IOPzrsbrwToGl6Vb2Vx4ha0aV2eOb5EaVSACvTLDp3715dfOcPha3sbPskovpdtrTXpt6m0cPKceb9TzOPQdUdSr25gXyPtQFw4iDoP4l3EZ/CqsVhdPp82oxp/o8Eixu+4DDNnHHXtTLveLh4mnMyxExo+7IKg8Y9q2PCXhyfxRqjaelw1vCEMsj7Sw4wBxkZPzfzr06tZ0KLrVZJRWuz269e236mMY80uWK1Me0tLjUb6G0t18y4ncIik4yx9zU17pdxp7Tx3WxJoJvJeLcCwOM547e9dvfeFvB0UF3/Z/iJzqFrEzLG8qgPIoOADgdx2JrGvNA0xdJtm+2XQ1aWAzFZI90dwxYAKh78E5OT0rjp5rTqyTjdJ6WcXfvf0t5fM0dBxWv5mLbWUeqTWlpp8ZW6ZG80zzqqMwyeCcYGOxNZ7KVZlPVTg4Oa6jwR4Zs/E2rXNjeTzwNFCZF8rGThgCDke4rnriB7O5ubdywkidojt6HBwQfyrspYiDrzoJ6xSdvW/XqvyM5QfKpdyvVvTp7O3ume9tTcxGN1CB9uGKkKc+xwaqV3/grwZoXiXT55bi+vRNAFMqx7UVM7uOQc8DOeKWYYujhaDqVr8u2l76+mw6VOU5WjucLH5HkTeYX83A8oDoeec/hTrtLaOVRaTvNGUUszx7CGxyMZPAPer/AIl0V/D/AIgutOYsyRtmJm6sh5U/XHX3BrtfB3w503XPD0Go6hPdpLOzlEidVGwHbnlSc5z+lYYrM8NhaEcXOT5JbW1vdXX5FQoznJwS1R5sHYKADjByMDnP1q9aX81qlxcbreaSdTC63EYkbBH3huHB96pTRmKeSM9UYr+Rq/oMemza1bQ6sZFspG2O8bbSmejdOgPX2rtrcnsnJq6tf16mcb81iB57M6VDAlqVvFlZpJ9/DIQMLj2IP51AZZXiSIszJHkqvZc9a7Pxl4KtNBu4IrGe5llvJFW1gaMEMOARvyOckcY6EUnjDQNN8I2dla21xO+qzxZuDvGwJjB4x3PTnoDXBQzTC1VT9ldupdrfpvvslt26I1lRnG/N0Ob/ALTj/wCEf/sxbG3Mhn843Xl/vQMY259KgstSurDUI76CUi4Rw+5uckHPOevIqOC5NvHMqL80qbN+SCB3H41HEqvKqvII1J5cgnH5V3qlBKScdH8733MuZ6E17d3GqX9xez/PNMxkkKrge/AprXlw9lHZtM5t43MiRk8Bj1P6Vqfb7TTdLgOkXl7HqEyPFfdBGyE8Be/SsSlRtJW5bJbfLTbp5eQS06hRRRXQQWbazeeNpn3R2qMFecozKpIOAcDvg1b0e80/T5rptQ0/7buhZIQW2hHPRsd6gshqN2jaZYrPMs7BzbxAtvKg4OB6AmkNrqF7Hc3hgnlSDAnl2EhOw3Ht0rmnaTlGpKy02dn5eerv1/Utd0iW31ADzTLZ28g8sgYhUbW7E8VYtfFGpWUvmWrRQvs8smKMJlfQ4xWZDMIo5l+f94u35X2jr3Hce1Kl26WUtoEiKSOrljGC4Iz0bqBzWk489+aN/X+v+HJWmx6T8QPsE+k6PrK2wk+1wkmeTLEnaGRDgj1bn2rkNrPZTpNFCWtoRMIixAQE4xhnBzyPug9a6vw+2neJPhu2j6nqlvYPaXP7qadl4GcjgkZ+8w61zniTwxp2kWC3dn4mstUkMgRooiu4DB+bh2yOAPxrwMtxXsP9hqSalGTSvFu6vda2stHbc6q1Pm/eJaNdzKtprRoZpZdOtGCLwv2h0bPqBuOa7vU7qW7+Hej+IYnZ7iwlCBc48nB2cEc9QnUnrXnOn3QsdQt7poI5xDIHMUoyr4PQ16J4dutJuPAmqaTPqtpHLdo1wsMhEYjkJOEXJ5wUU8f3q6M4nOm6dblvaS6X0d1JbO2nXS+xOHineN+nf7jh01S3eKSC4s08uRzIzLkuXwcck5xzW/4d8fXGieXaQWipZGTc8cXLEkAZGep4HGawtSs9LsNRmsra8+3RfKFuwCgT+9lec4+tM0iW1sfEdtJLczJbRTj9/Dw2AfvD045rsrxoYmg+anzJq6TW+na2j9VfyM480JaO3zO8ufBmkeJ7efV/D92txPIxeS2L+X8x5I5ztPPTp74rz+5MME7WtzZ3KSQMYyhuOUIPI+7xzmvTNO0/RtE1OG/XxqPsVvI0wtJSPMLOOc8gnIwfu1594u1K21fxVqF9aYNvLINhCkbgABnB9cZ/GvOyfG16laVFtyppXTcbNO9uV6K+muxriKUFFS2fr+O5sfD68gh8Y2qWqSQyTq8W+aQSKPlJ+6AueQO9N8U3Fvp2qa1o89qXaW9Fy0qkAqSCflyDgEN71X8Nm102Ox1W6uoYtt8rRqi7pDtK7g3PyqVY8+1db4l0bwr4i1uXUz4stLdpVUMgKt0AGc7h2AqcRi4Usy9pUi+RxtdRb96MrrVK/wCg4U3KjZPW/fo0eaZ08/wXK/8AA1P9BXe/DGXM+rWmnO6yS24YmTqMEgEY7/NXJJZ6JZ+J5LW+vJrjS42YfaLTG5+OCOo61sfDjVLPSfFsktxcLBayQPH5kxCjGQRn34rszap7fAVFCF/dUldaPW9vXTYzoR5aqu+tjc8Qi08VeErfxJNDK80KfZma3I3h9wGXUjGM54B/jFdPp88ula/pPh6NYjJbaY3ybyFbLLyTg4b5Dxj+I81xXgbXrDTda1TSb+eL+y7p2ZHdhsDKeDn3Hf2FS2XiW0l+L0upS3UaWJLwrMzYTaqEA59CR+teBicNUftMN7K9OEZTjvbVK0VruveOqElpPm1bSe39djk9Vs7b+3tQh8y581LiUMiW4YAhjnndkj3xVJoLOPcj3Eobj71vgj/x6uguTYz+M9bvY9aSzVHluLaZE3iVichRj1zWZaXL+IPEMbazeIfP+SW5uH2iNQPvDoMgDgdzX1FHFP2abjoopv4r3tfTo/vv0OKVPXfr5HrPhF5dW8NaVcXloblrOQ/ZZ5GCF8AqDjnoCR/wHNeb6/aX+ueJ9Ulm803UTM0sSwswhReByOwGOe/XvXSeJfHbWOoWek+GZ7ZbG3SMGTgoSCCBuPYAAH6mqvj+bS9Whg1vSdQhF48Yju7eKUbyvqcdcdD7Y9K+cyz2tDFKtKioqrfl+J8ut7NX05vLqdlZKUOVSvy77anC/Zrb/n/i/wC/b/4Vq3On2dno9vDcwiG8lLSpcSeam+M424XZgjg/nWJH5TAiQ7NqkqVXJZuwPNTXeo3V+kIu7iWZoUEcZd87UHQCvrKl5TjZaLfVr02evmcC0T1/IjlgjjTct3DKc/dQPn9VArWsTp8vh24NxLbRXVpIskMbQlmuc8FSwPAFZ32m0GmG3WxX7SWDG5aQkgDPAXpzn36UkP2T7BL5k0yXG8bUVcqy+/vWddOpHZxs1t/T0e3f0Kj7r7lUnLE4Ayeg7UVJ5Uf/AD3X/vk/4UVvzImw+xvrrTbpbqyuJIJ1BAdDgjIwaj8+bEg818SHLjcfm+vrV/TbYzWV/NHZi4aCHzHZ2wIl3AZxkZPNZuV2Ywd2eue1ZxcJTlZaqye3qvzG7pIsXc8FwyvDbLb4RVKISQSBgtkknJPNWLO602LSr6C6sGmvJQv2ecSlRDg88d81nsdzEhQvsOlJTdJSgo69Or6ef59w5ne5payZ5J7eaawSzD28YRY02hwFxv8AqcVStjAt1EbpJHgDDzFjYKxXvgkHmp/tEl7FHFd3pWO2jKwK4LADOdox05NQy27RbPnjfcu7924bH1x0NTTXLD2ctPS/5+g3q7otwWUOp6pNFZyLbQBZJI/tUgyFVS2CQOTx6VWurZbeQLHcRXC+Wrl4s4XIHByByM4p+nCwN039otMsHlvgwgbt+07evbOKjgvLi2jnjgmeNJ08uVVPDrnOD+IpJTU7ReiS3/z3b/rqGlhiQu8Ukg27Y8bssAeTjgd6W3V2uIxHF5r7gQmM7vbFRU+KWSCVZYnKOvRgeRWzTsySe/ulvbo3AVldxlwTkZ9vbGB+FVaKtM1iRaBY51IGLklwdx3dV4449c1KSppRS0HvqRpazOCdm0BC+W+XIHpnrVnToHuLiKK0s5Ly7Jb9x5ZYEY7AHOetauqeILSTTl0+wiuGghuBNbvdMGePgAgEYyDjoRxWXFqk9lqw1CxuJY5ySzP905P3hwenJrmjUr1abvHletr/AIXt/X5ltRi9yosMkskgChSgLMpOMAdRz/KpV+1wae7iJxa3LeWZCnDFcHAPqMimXtwl3ezXEcKwLI5YRqxYLn3PJpGu7h7NLRpnNvG5dIyflDHAJ/QV0WnJK67XT/re5GiNrS7CPxLPePdXltYm0st6bYlUSFAABjI5Pc1iygrDCrQeW2C285y4PQ/oelQ1paXavrGp29pL9qkXbsH2eLzHVRzwueg5rJxdHmnKXuLp2svxv5lX5tEtSmYAkUcryIVfPyowLD6jtUSEK6sVDAHJU961pE0pLXUIPPk82KT/AEZmtiHlGcEMd3y/TBrJ2tgHaeRkcVpSqc6d7/dbzJasdBqHh9dH1DT5NUdPsN3tlf7G25olJ5Xn+ID61QfUP7N1G9/sS6uYrSYNEpY4d4z2bFJdS20C2y2l3LdRkLLNHNFtCyDjHU5GOM1Nb6S+pWl3qnmw29vHOqMoViQX3EAADpxiuWPuwUsQ7rbayeunuvW/Q0ertD+vmZIBJ4BNaF5YQ22mWFwHufPuVZmSSDam0HAKtn5vyqLT7+50y8aa0ZfMKPFkrnIYFTwfY1LMLjSby3InLTRLkKyn93ntg/XtXRUlP2iSduvro9HpottSElYou0ZSMJGVYDDktncfX2plSQwvPMsSbdzdNzAD8zS20scN1FLLAs8aMC0TkgOPQkc1teyaWpJFRV2a8tpJ5HTTYI0ZiVQO5CjPT71FSpyt8L/D/Mdl3KgZ0Q7WIDjBAPUe9NooqxBV/R7KDUNTitbiaSGN85eNA5GAT0JH86KK58bUlTw1ScHZpN/gVTSc0mO0iwt9R1mOzmnliickCRIwzcA44JH86XTtYvNElu/sMigXETQOXjByh+vQ0UVin7avOjU1jyxdvNt/5Ir4YqS3u/0M2iiiu8yCrc13C9wskVjDEoiCGPLMCcYLcnOT1ooqXFN3Y7leaMwytGSCR6VJdtatKps45Uj2KGErhjux8x4A4zRRUrVxfl/kMhAycU+SUyhMqg2KFG1QM/X1PvRRV2VxEdFFFMQVas7+exE/kbA0ybC5QFlGQcqeqnjqKKKmUYyVpK6Gm1sVa2tMkk1GOaG61C5jjtLOQQqiBxtzkryRgHPvRRXLj5OFBzW62/IukrysZtvErJLNIm9IxyobacnoehqSy1S/sAEs7uWEeYsuEbA3rnB/U0UVu4RndSV0Sm1sTSXyR6fcWUllA91JNve8JYvj0Hbr3xWfIhjcqcZHpRRTpwUduuoN3G0UUVoSFFFFAH//2Q==",
    }

    def test_captcha(self):
        for k, v in self.test_captchas.items():
            self.assertEqual(decode_captcha(v), k)
