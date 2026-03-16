# def analyze_password(password,
#                      min_length = 8,
#                      require_digit = True,
#                      require_upper=True,
#                      require_symbol=False,
#                      banned_words=None):
#     if banned_words is None:
#         banned_words = ["heslo", "password", "1234"]
#     symbols = "!@#$%^&*()-_=+[]{};:,.?"
#     total_rules = 0
#     passed_rules = 0
#     missing_rules = []
#
#     total_rules += 1
#     if len(password) >= min_length:
#         passed_rules += 1
#     else: missing_rules.append("min_length")
#
#     if require_digit:
#         total_rules += 1
#         if any(c.isdigit() for c in password):
#             passed_rules += 1
#         else: missing_rules.append("digit")
#
#     if require_upper:
#         total_rules += 1
#         if any(c.isupper() for c in password):
#             passed_rules += 1
#         else: missing_rules.append("upper")
#
#     total_rules +=1
#     if not any(word.lower() in password.lower() for word in banned_words):
#         passed_rules += 1
#     else: missing_rules.append("banned_word")
#
#     score_percent = int((passed_rules / total_rules) * 100)
#     is_strong =  passed_rules == total_rules
#
#     return is_strong, score_percent, missing_rules
#
# result1= analyze_password("Password1")
# print("Test 1:", result1)
# print(" Je citelne, protoze paramtery dodrzuji dane funkci")
#
# result2 = analyze_password("Password1", require_symbol=True)
# print("Test 2:", result2)
# print("citelne protoze dulezite pravidla jsou dodrzeny")
#
#
# result3 = analyze_password("Password1", require_symbol=False)
# print("Test 3:", result3)
# print("citelne protoze dulezite pravidla jsou dodrzeny")
#
# result4 = analyze_password("Admin123!", banned_words=["admin", "root"])
# print("Test 4:", result4)
# print("spravne zkontoloval")