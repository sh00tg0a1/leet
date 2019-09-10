from queue import deque
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        rules = deque()

        last_rule = ''
        for i, v in enumerate(p):
            if v in '*':
                if last_rule:
                    last_rule += v
                    rules.append(last_rule)
                else:
                    rules.append(v)
                last_rule = ''

            else:
                if last_rule:
                    rules.append(last_rule)
                last_rule = v

        if last_rule:
            rules.append(last_rule)

        cur_index = 0
        while len(rules) != 0:
            rule = rules.popleft()
            rule_matched = False

            if cur_index == len(s):
                if '*' not in rule:
                    return False

            for i in range(cur_index, len(s)):
                if len(rule) == 1:
                    if rule == '.':
                        cur_index += 1
                        rule_matched = True
                    else:
                        if s[cur_index] == rule:
                            cur_index += 1
                            rule_matched = True
                    break
                else:
                    if rule[0] == '.':
                        cur_index += 1
                        rule_matched = True
                    else:
                        rule_matched = True

                        if s[cur_index] == rule[0]:
                            cur_index += 1
                        else:
                            break

            #
            # if not rule_matched:
            #     return False

        return cur_index == len(s)
