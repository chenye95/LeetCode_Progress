"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is
 a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common
 email to both accounts. Note that even if two accounts have the same name, they may belong to different people as
 people could have the same name. A person can have any number of accounts initially, but all of their accounts
 definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name,
 and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
"""
from collections import defaultdict
from typing import List, DefaultDict

from _Union_Find import UnionFindArray


def accounts_merge_dfs(accounts: List[List[str]]) -> List[List[str]]:
    """
    :param accounts: List of ["name", "email1", "email2", ...].
        - 1 <= len(accounts) <= 1000
        - 2 <= len(accounts[i]) <= 10
        - 1 <= len(accounts[i][j]) <= 30
    :return: post merge list of ["name", "email1", "email2", ...] where emails are sorted. Accounts can be returned in
        any order
    """
    email_to_name_lookup = {}
    email_connections = defaultdict(set)

    for account_i in accounts:
        person_name = account_i[0]
        main_email = account_i[1]
        email_to_name_lookup[main_email] = person_name
        for email in account_i[2:]:
            email_connections[main_email].add(email)
            email_connections[email].add(main_email)
            email_to_name_lookup[email] = person_name

    seen_emails = set()
    post_merge_accounts = []
    for email in email_to_name_lookup:
        if email not in seen_emails:
            seen_emails.add(email)
            related_emails = [email]
            belong_to_same_person = [email]
            while related_emails:
                current_email = related_emails.pop()
                next_emails = [next_email for next_email in email_connections[current_email]
                               if next_email not in seen_emails]
                related_emails.extend(next_emails)
                belong_to_same_person.extend(next_emails)
                seen_emails.update(set(next_emails))
            post_merge_accounts.append([email_to_name_lookup[email]] + sorted(list(belong_to_same_person)))

    return post_merge_accounts


def accounts_merge_union_find(accounts: List[List[str]]) -> List[List[str]]:
    """
    :param accounts: List of ["name", "email1", "email2", ...].
        - 1 <= len(accounts) <= 1000
        - 2 <= len(accounts[i]) <= 10
        - 1 <= len(accounts[i][j]) <= 30
    :return: post merge list of ["name", "email1", "email2", ...] where emails are sorted. Accounts can be returned in
        any order
    """
    union_find_object = UnionFindArray(10001, True)
    email_to_name_lookup = {}
    email_to_id_lookup = {}
    counter = 0

    for account_i in accounts:
        person_name = account_i[0]
        main_email = account_i[1]

        if main_email not in email_to_id_lookup:
            email_to_name_lookup[main_email] = person_name
            email_to_id_lookup[main_email] = main_email_id = counter
            counter += 1
        else:
            main_email_id = email_to_id_lookup[main_email]

        for email in account_i[2:]:
            if email not in email_to_id_lookup:
                email_to_name_lookup[email] = person_name
                email_to_id_lookup[email] = mail_id = counter
                counter += 1
            else:
                mail_id = email_to_id_lookup[email]
            union_find_object.unify(main_email_id, mail_id)

    union_id_emails: DefaultDict[int, List[str]] = defaultdict(list)
    for email in email_to_id_lookup:
        union_id_emails[union_find_object.find(email_to_id_lookup[email])].append(email)

    return [[email_to_name_lookup[email_list[0]]] + sorted(email_list) for email_list in union_id_emails.values()]


test_cases = [([["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"]],
               [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"]]),
              ([["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
                ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
                ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
                ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
                ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]],
               [["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
                ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
                ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
                ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
                ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"]]),
              ([["David", "David35@m.co", "David38@m.co", "David85@m.co", "David9@m.co", "David38@m.co", "David3@m.co",
                 "David13@m.co", "David64@m.co", "David16@m.co"],
                ["Isa", "Isa74@m.co", "Isa21@m.co", "Isa26@m.co", "Isa82@m.co", "Isa66@m.co", "Isa74@m.co",
                 "Isa63@m.co", "Isa75@m.co", "Isa6@m.co"],
                ["Bob", "Bob96@m.co", "Bob74@m.co", "Bob84@m.co", "Bob15@m.co", "Bob49@m.co", "Bob17@m.co",
                 "Bob14@m.co", "Bob50@m.co", "Bob85@m.co"],
                ["John", "John76@m.co", "John0@m.co", "John93@m.co", "John79@m.co", "John89@m.co", "John64@m.co",
                 "John70@m.co", "John44@m.co", "John19@m.co"],
                ["Lily", "Lily19@m.co", "Lily69@m.co", "Lily26@m.co", "Lily22@m.co", "Lily81@m.co", "Lily39@m.co",
                 "Lily11@m.co", "Lily47@m.co", "Lily61@m.co"],
                ["David", "David89@m.co", "David28@m.co", "David87@m.co", "David94@m.co", "David91@m.co",
                 "David81@m.co", "David26@m.co", "David23@m.co", "David68@m.co"],
                ["Bob", "Bob70@m.co", "Bob78@m.co", "Bob93@m.co", "Bob82@m.co", "Bob95@m.co", "Bob73@m.co",
                 "Bob63@m.co", "Bob3@m.co", "Bob95@m.co"],
                ["David", "David77@m.co", "David3@m.co", "David42@m.co", "David13@m.co", "David51@m.co", "David41@m.co",
                 "David72@m.co", "David7@m.co", "David35@m.co"],
                ["John", "John39@m.co", "John21@m.co", "John61@m.co", "John21@m.co", "John68@m.co", "John65@m.co",
                 "John81@m.co", "John3@m.co", "John54@m.co"],
                ["Ethan", "Ethan42@m.co", "Ethan41@m.co", "Ethan56@m.co", "Ethan66@m.co", "Ethan16@m.co",
                 "Ethan14@m.co", "Ethan60@m.co", "Ethan2@m.co", "Ethan69@m.co"],
                ["David", "David76@m.co", "David98@m.co", "David8@m.co", "David67@m.co", "David39@m.co", "David96@m.co",
                 "David24@m.co", "David98@m.co", "David29@m.co"],
                ["Bob", "Bob54@m.co", "Bob95@m.co", "Bob2@m.co", "Bob66@m.co", "Bob39@m.co", "Bob87@m.co", "Bob71@m.co",
                 "Bob99@m.co", "Bob31@m.co"],
                ["Ethan", "Ethan78@m.co", "Ethan92@m.co", "Ethan20@m.co", "Ethan76@m.co", "Ethan77@m.co",
                 "Ethan86@m.co", "Ethan87@m.co", "Ethan74@m.co", "Ethan69@m.co"],
                ["Gabe", "Gabe14@m.co", "Gabe83@m.co", "Gabe10@m.co", "Gabe84@m.co", "Gabe24@m.co", "Gabe80@m.co",
                 "Gabe41@m.co", "Gabe67@m.co", "Gabe71@m.co"],
                ["Ethan", "Ethan19@m.co", "Ethan98@m.co", "Ethan75@m.co", "Ethan88@m.co", "Ethan0@m.co", "Ethan71@m.co",
                 "Ethan6@m.co", "Ethan92@m.co", "Ethan21@m.co"],
                ["Ethan", "Ethan73@m.co", "Ethan96@m.co", "Ethan99@m.co", "Ethan63@m.co", "Ethan7@m.co", "Ethan48@m.co",
                 "Ethan64@m.co", "Ethan50@m.co", "Ethan14@m.co"],
                ["Ethan", "Ethan7@m.co", "Ethan18@m.co", "Ethan81@m.co", "Ethan69@m.co", "Ethan59@m.co", "Ethan37@m.co",
                 "Ethan30@m.co", "Ethan20@m.co", "Ethan30@m.co"],
                ["Bob", "Bob36@m.co", "Bob0@m.co", "Bob61@m.co", "Bob71@m.co", "Bob41@m.co", "Bob31@m.co", "Bob39@m.co",
                 "Bob56@m.co", "Bob43@m.co"],
                ["Bob", "Bob8@m.co", "Bob21@m.co", "Bob81@m.co", "Bob85@m.co", "Bob21@m.co", "Bob12@m.co", "Bob27@m.co",
                 "Bob78@m.co", "Bob99@m.co"],
                ["Lily", "Lily4@m.co", "Lily78@m.co", "Lily1@m.co", "Lily11@m.co", "Lily22@m.co", "Lily52@m.co",
                 "Lily46@m.co", "Lily96@m.co", "Lily49@m.co"],
                ["Lily", "Lily49@m.co", "Lily81@m.co", "Lily96@m.co", "Lily11@m.co", "Lily70@m.co", "Lily68@m.co",
                 "Lily73@m.co", "Lily45@m.co", "Lily84@m.co"],
                ["Gabe", "Gabe23@m.co", "Gabe54@m.co", "Gabe71@m.co", "Gabe32@m.co", "Gabe35@m.co", "Gabe100@m.co",
                 "Gabe30@m.co", "Gabe42@m.co", "Gabe65@m.co"],
                ["Hanzo", "Hanzo37@m.co", "Hanzo15@m.co", "Hanzo79@m.co", "Hanzo93@m.co", "Hanzo35@m.co",
                 "Hanzo26@m.co", "Hanzo86@m.co", "Hanzo19@m.co", "Hanzo94@m.co"],
                ["Hanzo", "Hanzo71@m.co", "Hanzo70@m.co", "Hanzo56@m.co", "Hanzo47@m.co", "Hanzo68@m.co",
                 "Hanzo39@m.co", "Hanzo16@m.co", "Hanzo56@m.co", "Hanzo35@m.co"],
                ["Kevin", "Kevin83@m.co", "Kevin1@m.co", "Kevin14@m.co", "Kevin96@m.co", "Kevin75@m.co", "Kevin97@m.co",
                 "Kevin41@m.co", "Kevin79@m.co", "Kevin85@m.co"],
                ["Bob", "Bob59@m.co", "Bob54@m.co", "Bob9@m.co", "Bob92@m.co", "Bob7@m.co", "Bob0@m.co", "Bob30@m.co",
                 "Bob43@m.co", "Bob56@m.co"],
                ["Gabe", "Gabe43@m.co", "Gabe21@m.co", "Gabe13@m.co", "Gabe98@m.co", "Gabe4@m.co", "Gabe99@m.co",
                 "Gabe60@m.co", "Gabe21@m.co", "Gabe78@m.co"],
                ["Hanzo", "Hanzo0@m.co", "Hanzo51@m.co", "Hanzo22@m.co", "Hanzo3@m.co", "Hanzo64@m.co", "Hanzo76@m.co",
                 "Hanzo65@m.co", "Hanzo64@m.co", "Hanzo94@m.co"],
                ["Ethan", "Ethan19@m.co", "Ethan21@m.co", "Ethan58@m.co", "Ethan62@m.co", "Ethan74@m.co",
                 "Ethan73@m.co", "Ethan97@m.co", "Ethan38@m.co", "Ethan93@m.co"],
                ["Fern", "Fern49@m.co", "Fern44@m.co", "Fern26@m.co", "Fern52@m.co", "Fern100@m.co", "Fern92@m.co",
                 "Fern23@m.co", "Fern66@m.co", "Fern84@m.co"],
                ["David", "David84@m.co", "David78@m.co", "David78@m.co", "David41@m.co", "David4@m.co", "David82@m.co",
                 "David32@m.co", "David83@m.co", "David93@m.co"],
                ["Ethan", "Ethan59@m.co", "Ethan9@m.co", "Ethan25@m.co", "Ethan5@m.co", "Ethan39@m.co", "Ethan38@m.co",
                 "Ethan53@m.co", "Ethan16@m.co", "Ethan83@m.co"],
                ["David", "David100@m.co", "David87@m.co", "David68@m.co", "David88@m.co", "David34@m.co",
                 "David82@m.co", "David10@m.co", "David76@m.co", "David70@m.co"],
                ["Fern", "Fern75@m.co", "Fern66@m.co", "Fern100@m.co", "Fern50@m.co", "Fern89@m.co", "Fern0@m.co",
                 "Fern78@m.co", "Fern55@m.co", "Fern74@m.co"],
                ["Fern", "Fern94@m.co", "Fern46@m.co", "Fern44@m.co", "Fern29@m.co", "Fern87@m.co", "Fern83@m.co",
                 "Fern66@m.co", "Fern88@m.co", "Fern62@m.co"],
                ["Ethan", "Ethan88@m.co", "Ethan22@m.co", "Ethan12@m.co", "Ethan3@m.co", "Ethan12@m.co", "Ethan14@m.co",
                 "Ethan58@m.co", "Ethan63@m.co", "Ethan43@m.co"],
                ["Ethan", "Ethan28@m.co", "Ethan41@m.co", "Ethan23@m.co", "Ethan50@m.co", "Ethan91@m.co",
                 "Ethan94@m.co", "Ethan46@m.co", "Ethan80@m.co", "Ethan65@m.co"],
                ["John", "John15@m.co", "John32@m.co", "John69@m.co", "John48@m.co", "John3@m.co", "John50@m.co",
                 "John31@m.co", "John75@m.co", "John37@m.co"],
                ["Gabe", "Gabe28@m.co", "Gabe26@m.co", "Gabe61@m.co", "Gabe42@m.co", "Gabe52@m.co", "Gabe18@m.co",
                 "Gabe85@m.co", "Gabe9@m.co", "Gabe84@m.co"],
                ["Alex", "Alex54@m.co", "Alex59@m.co", "Alex10@m.co", "Alex93@m.co", "Alex71@m.co", "Alex5@m.co",
                 "Alex68@m.co", "Alex83@m.co", "Alex87@m.co"],
                ["Gabe", "Gabe35@m.co", "Gabe12@m.co", "Gabe49@m.co", "Gabe81@m.co", "Gabe33@m.co", "Gabe30@m.co",
                 "Gabe56@m.co", "Gabe29@m.co", "Gabe77@m.co"],
                ["Gabe", "Gabe37@m.co", "Gabe37@m.co", "Gabe96@m.co", "Gabe44@m.co", "Gabe99@m.co", "Gabe90@m.co",
                 "Gabe43@m.co", "Gabe99@m.co", "Gabe16@m.co"],
                ["Ethan", "Ethan22@m.co", "Ethan58@m.co", "Ethan43@m.co", "Ethan87@m.co", "Ethan64@m.co",
                 "Ethan94@m.co", "Ethan69@m.co", "Ethan55@m.co", "Ethan65@m.co"],
                ["David", "David42@m.co", "David47@m.co", "David56@m.co", "David56@m.co", "David51@m.co", "David4@m.co",
                 "David95@m.co", "David75@m.co", "David79@m.co"],
                ["David", "David78@m.co", "David40@m.co", "David84@m.co", "David51@m.co", "David81@m.co",
                 "David13@m.co", "David98@m.co", "David47@m.co", "David38@m.co"],
                ["Hanzo", "Hanzo100@m.co", "Hanzo23@m.co", "Hanzo49@m.co", "Hanzo99@m.co", "Hanzo79@m.co",
                 "Hanzo53@m.co", "Hanzo4@m.co", "Hanzo10@m.co", "Hanzo20@m.co"],
                ["Bob", "Bob92@m.co", "Bob22@m.co", "Bob32@m.co", "Bob88@m.co", "Bob89@m.co", "Bob29@m.co",
                 "Bob83@m.co", "Bob27@m.co", "Bob97@m.co"],
                ["Lily", "Lily8@m.co", "Lily1@m.co", "Lily80@m.co", "Lily33@m.co", "Lily92@m.co", "Lily49@m.co",
                 "Lily75@m.co", "Lily49@m.co", "Lily61@m.co"],
                ["Ethan", "Ethan16@m.co", "Ethan62@m.co", "Ethan12@m.co", "Ethan45@m.co", "Ethan27@m.co",
                 "Ethan35@m.co", "Ethan40@m.co", "Ethan55@m.co", "Ethan37@m.co"],
                ["Celine", "Celine46@m.co", "Celine79@m.co", "Celine46@m.co", "Celine43@m.co", "Celine60@m.co",
                 "Celine99@m.co", "Celine0@m.co", "Celine31@m.co", "Celine86@m.co"],
                ["John", "John47@m.co", "John6@m.co", "John21@m.co", "John46@m.co", "John83@m.co", "John54@m.co",
                 "John30@m.co", "John93@m.co", "John52@m.co"],
                ["Fern", "Fern68@m.co", "Fern6@m.co", "Fern98@m.co", "Fern60@m.co", "Fern29@m.co", "Fern46@m.co",
                 "Fern43@m.co", "Fern37@m.co", "Fern68@m.co"],
                ["Gabe", "Gabe85@m.co", "Gabe87@m.co", "Gabe13@m.co", "Gabe35@m.co", "Gabe35@m.co", "Gabe79@m.co",
                 "Gabe25@m.co", "Gabe25@m.co", "Gabe26@m.co"],
                ["Isa", "Isa15@m.co", "Isa24@m.co", "Isa75@m.co", "Isa84@m.co", "Isa58@m.co", "Isa93@m.co",
                 "Isa65@m.co", "Isa44@m.co", "Isa14@m.co"],
                ["Bob", "Bob9@m.co", "Bob64@m.co", "Bob24@m.co", "Bob10@m.co", "Bob56@m.co", "Bob30@m.co", "Bob92@m.co",
                 "Bob34@m.co", "Bob37@m.co"],
                ["Lily", "Lily64@m.co", "Lily64@m.co", "Lily62@m.co", "Lily18@m.co", "Lily57@m.co", "Lily95@m.co",
                 "Lily60@m.co", "Lily78@m.co", "Lily90@m.co"],
                ["Fern", "Fern7@m.co", "Fern44@m.co", "Fern61@m.co", "Fern23@m.co", "Fern99@m.co", "Fern71@m.co",
                 "Fern31@m.co", "Fern97@m.co", "Fern14@m.co"],
                ["Isa", "Isa7@m.co", "Isa33@m.co", "Isa22@m.co", "Isa92@m.co", "Isa50@m.co", "Isa20@m.co", "Isa4@m.co",
                 "Isa22@m.co", "Isa13@m.co"],
                ["Gabe", "Gabe29@m.co", "Gabe27@m.co", "Gabe49@m.co", "Gabe89@m.co", "Gabe75@m.co", "Gabe77@m.co",
                 "Gabe76@m.co", "Gabe21@m.co", "Gabe95@m.co"],
                ["Isa", "Isa38@m.co", "Isa4@m.co", "Isa58@m.co", "Isa11@m.co", "Isa47@m.co", "Isa39@m.co", "Isa6@m.co",
                 "Isa96@m.co", "Isa4@m.co"],
                ["Isa", "Isa66@m.co", "Isa36@m.co", "Isa44@m.co", "Isa49@m.co", "Isa49@m.co", "Isa3@m.co", "Isa50@m.co",
                 "Isa91@m.co", "Isa96@m.co"],
                ["Fern", "Fern27@m.co", "Fern43@m.co", "Fern25@m.co", "Fern48@m.co", "Fern2@m.co", "Fern48@m.co",
                 "Fern87@m.co", "Fern95@m.co", "Fern91@m.co"],
                ["Isa", "Isa1@m.co", "Isa100@m.co", "Isa95@m.co", "Isa58@m.co", "Isa17@m.co", "Isa31@m.co",
                 "Isa97@m.co", "Isa28@m.co", "Isa37@m.co"],
                ["David", "David79@m.co", "David19@m.co", "David56@m.co", "David98@m.co", "David67@m.co",
                 "David23@m.co", "David77@m.co", "David60@m.co", "David79@m.co"],
                ["David", "David100@m.co", "David53@m.co", "David37@m.co", "David83@m.co", "David21@m.co",
                 "David43@m.co", "David63@m.co", "David33@m.co", "David2@m.co"],
                ["Isa", "Isa2@m.co", "Isa47@m.co", "Isa23@m.co", "Isa56@m.co", "Isa9@m.co", "Isa100@m.co", "Isa28@m.co",
                 "Isa25@m.co", "Isa16@m.co"],
                ["Lily", "Lily83@m.co", "Lily4@m.co", "Lily77@m.co", "Lily77@m.co", "Lily85@m.co", "Lily20@m.co",
                 "Lily69@m.co", "Lily21@m.co", "Lily39@m.co"],
                ["Kevin", "Kevin21@m.co", "Kevin76@m.co", "Kevin55@m.co", "Kevin20@m.co", "Kevin7@m.co", "Kevin43@m.co",
                 "Kevin96@m.co", "Kevin20@m.co", "Kevin84@m.co"],
                ["Lily", "Lily73@m.co", "Lily67@m.co", "Lily74@m.co", "Lily71@m.co", "Lily1@m.co", "Lily57@m.co",
                 "Lily38@m.co", "Lily6@m.co", "Lily66@m.co"],
                ["Celine", "Celine13@m.co", "Celine23@m.co", "Celine3@m.co", "Celine61@m.co", "Celine69@m.co",
                 "Celine42@m.co", "Celine74@m.co", "Celine27@m.co", "Celine10@m.co"],
                ["Hanzo", "Hanzo0@m.co", "Hanzo32@m.co", "Hanzo97@m.co", "Hanzo79@m.co", "Hanzo22@m.co", "Hanzo59@m.co",
                 "Hanzo93@m.co", "Hanzo42@m.co", "Hanzo55@m.co"],
                ["John", "John53@m.co", "John17@m.co", "John5@m.co", "John25@m.co", "John42@m.co", "John43@m.co",
                 "John96@m.co", "John31@m.co", "John32@m.co"],
                ["Bob", "Bob66@m.co", "Bob97@m.co", "Bob65@m.co", "Bob58@m.co", "Bob83@m.co", "Bob91@m.co",
                 "Bob38@m.co", "Bob83@m.co", "Bob28@m.co"],
                ["Hanzo", "Hanzo2@m.co", "Hanzo0@m.co", "Hanzo85@m.co", "Hanzo18@m.co", "Hanzo1@m.co", "Hanzo16@m.co",
                 "Hanzo70@m.co", "Hanzo19@m.co", "Hanzo88@m.co"],
                ["Kevin", "Kevin54@m.co", "Kevin76@m.co", "Kevin11@m.co", "Kevin58@m.co", "Kevin100@m.co",
                 "Kevin61@m.co", "Kevin77@m.co", "Kevin45@m.co", "Kevin31@m.co"],
                ["Ethan", "Ethan45@m.co", "Ethan11@m.co", "Ethan73@m.co", "Ethan6@m.co", "Ethan32@m.co", "Ethan55@m.co",
                 "Ethan81@m.co", "Ethan88@m.co", "Ethan25@m.co"],
                ["Kevin", "Kevin25@m.co", "Kevin83@m.co", "Kevin95@m.co", "Kevin28@m.co", "Kevin26@m.co",
                 "Kevin13@m.co", "Kevin99@m.co", "Kevin73@m.co", "Kevin15@m.co"],
                ["Fern", "Fern13@m.co", "Fern24@m.co", "Fern5@m.co", "Fern37@m.co", "Fern6@m.co", "Fern61@m.co",
                 "Fern87@m.co", "Fern22@m.co", "Fern21@m.co"],
                ["Celine", "Celine76@m.co", "Celine96@m.co", "Celine67@m.co", "Celine67@m.co", "Celine41@m.co",
                 "Celine8@m.co", "Celine75@m.co", "Celine79@m.co", "Celine66@m.co"],
                ["Fern", "Fern47@m.co", "Fern34@m.co", "Fern18@m.co", "Fern58@m.co", "Fern11@m.co", "Fern61@m.co",
                 "Fern43@m.co", "Fern69@m.co", "Fern77@m.co"],
                ["Alex", "Alex30@m.co", "Alex59@m.co", "Alex83@m.co", "Alex10@m.co", "Alex11@m.co", "Alex14@m.co",
                 "Alex24@m.co", "Alex74@m.co", "Alex31@m.co"],
                ["Gabe", "Gabe47@m.co", "Gabe33@m.co", "Gabe90@m.co", "Gabe53@m.co", "Gabe36@m.co", "Gabe14@m.co",
                 "Gabe32@m.co", "Gabe84@m.co", "Gabe92@m.co"],
                ["Bob", "Bob48@m.co", "Bob84@m.co", "Bob70@m.co", "Bob50@m.co", "Bob49@m.co", "Bob3@m.co", "Bob56@m.co",
                 "Bob78@m.co", "Bob9@m.co"],
                ["Lily", "Lily6@m.co", "Lily74@m.co", "Lily93@m.co", "Lily98@m.co", "Lily7@m.co", "Lily34@m.co",
                 "Lily5@m.co", "Lily78@m.co", "Lily57@m.co"],
                ["John", "John97@m.co", "John54@m.co", "John33@m.co", "John91@m.co", "John93@m.co", "John86@m.co",
                 "John74@m.co", "John14@m.co", "John11@m.co"],
                ["Lily", "Lily92@m.co", "Lily37@m.co", "Lily98@m.co", "Lily43@m.co", "Lily10@m.co", "Lily39@m.co",
                 "Lily88@m.co", "Lily78@m.co", "Lily19@m.co"],
                ["Alex", "Alex1@m.co", "Alex70@m.co", "Alex49@m.co", "Alex41@m.co", "Alex53@m.co", "Alex83@m.co",
                 "Alex67@m.co", "Alex46@m.co", "Alex90@m.co"],
                ["Hanzo", "Hanzo45@m.co", "Hanzo94@m.co", "Hanzo95@m.co", "Hanzo44@m.co", "Hanzo15@m.co",
                 "Hanzo67@m.co", "Hanzo62@m.co", "Hanzo85@m.co", "Hanzo89@m.co"],
                ["John", "John76@m.co", "John53@m.co", "John22@m.co", "John46@m.co", "John10@m.co", "John23@m.co",
                 "John86@m.co", "John61@m.co", "John88@m.co"],
                ["Celine", "Celine91@m.co", "Celine74@m.co", "Celine55@m.co", "Celine49@m.co", "Celine86@m.co",
                 "Celine3@m.co", "Celine68@m.co", "Celine43@m.co", "Celine53@m.co"],
                ["John", "John77@m.co", "John51@m.co", "John69@m.co", "John7@m.co", "John10@m.co", "John66@m.co",
                 "John26@m.co", "John86@m.co", "John57@m.co"],
                ["Ethan", "Ethan20@m.co", "Ethan33@m.co", "Ethan48@m.co", "Ethan81@m.co", "Ethan1@m.co", "Ethan69@m.co",
                 "Ethan65@m.co", "Ethan32@m.co", "Ethan58@m.co"],
                ["Hanzo", "Hanzo7@m.co", "Hanzo65@m.co", "Hanzo25@m.co", "Hanzo58@m.co", "Hanzo12@m.co", "Hanzo0@m.co",
                 "Hanzo28@m.co", "Hanzo20@m.co", "Hanzo81@m.co"],
                ["Celine", "Celine49@m.co", "Celine6@m.co", "Celine21@m.co", "Celine32@m.co", "Celine8@m.co",
                 "Celine81@m.co", "Celine68@m.co", "Celine12@m.co", "Celine27@m.co"],
                ["Kevin", "Kevin7@m.co", "Kevin33@m.co", "Kevin0@m.co", "Kevin5@m.co", "Kevin97@m.co", "Kevin33@m.co",
                 "Kevin60@m.co", "Kevin88@m.co", "Kevin3@m.co"],
                ["David", "David26@m.co", "David53@m.co", "David48@m.co", "David74@m.co", "David30@m.co",
                 "David71@m.co", "David36@m.co", "David97@m.co", "David13@m.co"],
                ["David", "David74@m.co", "David40@m.co", "David86@m.co", "David24@m.co", "David95@m.co",
                 "David84@m.co", "David96@m.co", "David61@m.co", "David45@m.co"],
                ["Lily", "Lily1@m.co", "Lily70@m.co", "Lily31@m.co", "Lily15@m.co", "Lily33@m.co", "Lily50@m.co",
                 "Lily29@m.co", "Lily71@m.co", "Lily1@m.co"],
                ["Ethan", "Ethan62@m.co", "Ethan14@m.co", "Ethan24@m.co", "Ethan25@m.co", "Ethan3@m.co", "Ethan83@m.co",
                 "Ethan78@m.co", "Ethan13@m.co", "Ethan60@m.co"],
                ["Ethan", "Ethan41@m.co", "Ethan34@m.co", "Ethan99@m.co", "Ethan25@m.co", "Ethan86@m.co",
                 "Ethan82@m.co", "Ethan9@m.co", "Ethan1@m.co", "Ethan66@m.co"]],
               [['David', 'David100@m.co', 'David10@m.co', 'David13@m.co', 'David16@m.co', 'David19@m.co',
                 'David21@m.co', 'David23@m.co', 'David24@m.co', 'David26@m.co', 'David28@m.co', 'David29@m.co',
                 'David2@m.co', 'David30@m.co', 'David32@m.co', 'David33@m.co', 'David34@m.co', 'David35@m.co',
                 'David36@m.co', 'David37@m.co', 'David38@m.co', 'David39@m.co', 'David3@m.co', 'David40@m.co',
                 'David41@m.co', 'David42@m.co', 'David43@m.co', 'David45@m.co', 'David47@m.co', 'David48@m.co',
                 'David4@m.co', 'David51@m.co', 'David53@m.co', 'David56@m.co', 'David60@m.co', 'David61@m.co',
                 'David63@m.co', 'David64@m.co', 'David67@m.co', 'David68@m.co', 'David70@m.co', 'David71@m.co',
                 'David72@m.co', 'David74@m.co', 'David75@m.co', 'David76@m.co', 'David77@m.co', 'David78@m.co',
                 'David79@m.co', 'David7@m.co', 'David81@m.co', 'David82@m.co', 'David83@m.co', 'David84@m.co',
                 'David85@m.co', 'David86@m.co', 'David87@m.co', 'David88@m.co', 'David89@m.co', 'David8@m.co',
                 'David91@m.co', 'David93@m.co', 'David94@m.co', 'David95@m.co', 'David96@m.co', 'David97@m.co',
                 'David98@m.co', 'David9@m.co'],
                ['Isa', 'Isa100@m.co', 'Isa11@m.co', 'Isa13@m.co', 'Isa14@m.co', 'Isa15@m.co', 'Isa16@m.co',
                 'Isa17@m.co', 'Isa1@m.co', 'Isa20@m.co', 'Isa21@m.co', 'Isa22@m.co', 'Isa23@m.co', 'Isa24@m.co',
                 'Isa25@m.co', 'Isa26@m.co', 'Isa28@m.co', 'Isa2@m.co', 'Isa31@m.co', 'Isa33@m.co', 'Isa36@m.co',
                 'Isa37@m.co', 'Isa38@m.co', 'Isa39@m.co', 'Isa3@m.co', 'Isa44@m.co', 'Isa47@m.co', 'Isa49@m.co',
                 'Isa4@m.co', 'Isa50@m.co', 'Isa56@m.co', 'Isa58@m.co', 'Isa63@m.co', 'Isa65@m.co', 'Isa66@m.co',
                 'Isa6@m.co', 'Isa74@m.co', 'Isa75@m.co', 'Isa7@m.co', 'Isa82@m.co', 'Isa84@m.co', 'Isa91@m.co',
                 'Isa92@m.co', 'Isa93@m.co', 'Isa95@m.co', 'Isa96@m.co', 'Isa97@m.co', 'Isa9@m.co'],
                ['Bob', 'Bob0@m.co', 'Bob10@m.co', 'Bob12@m.co', 'Bob14@m.co', 'Bob15@m.co', 'Bob17@m.co', 'Bob21@m.co',
                 'Bob22@m.co', 'Bob24@m.co', 'Bob27@m.co', 'Bob28@m.co', 'Bob29@m.co', 'Bob2@m.co', 'Bob30@m.co',
                 'Bob31@m.co', 'Bob32@m.co', 'Bob34@m.co', 'Bob36@m.co', 'Bob37@m.co', 'Bob38@m.co', 'Bob39@m.co',
                 'Bob3@m.co', 'Bob41@m.co', 'Bob43@m.co', 'Bob48@m.co', 'Bob49@m.co', 'Bob50@m.co', 'Bob54@m.co',
                 'Bob56@m.co', 'Bob58@m.co', 'Bob59@m.co', 'Bob61@m.co', 'Bob63@m.co', 'Bob64@m.co', 'Bob65@m.co',
                 'Bob66@m.co', 'Bob70@m.co', 'Bob71@m.co', 'Bob73@m.co', 'Bob74@m.co', 'Bob78@m.co', 'Bob7@m.co',
                 'Bob81@m.co', 'Bob82@m.co', 'Bob83@m.co', 'Bob84@m.co', 'Bob85@m.co', 'Bob87@m.co', 'Bob88@m.co',
                 'Bob89@m.co', 'Bob8@m.co', 'Bob91@m.co', 'Bob92@m.co', 'Bob93@m.co', 'Bob95@m.co', 'Bob96@m.co',
                 'Bob97@m.co', 'Bob99@m.co', 'Bob9@m.co'],
                ['John', 'John0@m.co', 'John10@m.co', 'John11@m.co', 'John14@m.co', 'John15@m.co', 'John17@m.co',
                 'John19@m.co', 'John21@m.co', 'John22@m.co', 'John23@m.co', 'John25@m.co', 'John26@m.co',
                 'John30@m.co', 'John31@m.co', 'John32@m.co', 'John33@m.co', 'John37@m.co', 'John39@m.co', 'John3@m.co',
                 'John42@m.co', 'John43@m.co', 'John44@m.co', 'John46@m.co', 'John47@m.co', 'John48@m.co',
                 'John50@m.co', 'John51@m.co', 'John52@m.co', 'John53@m.co', 'John54@m.co', 'John57@m.co', 'John5@m.co',
                 'John61@m.co', 'John64@m.co', 'John65@m.co', 'John66@m.co', 'John68@m.co', 'John69@m.co', 'John6@m.co',
                 'John70@m.co', 'John74@m.co', 'John75@m.co', 'John76@m.co', 'John77@m.co', 'John79@m.co', 'John7@m.co',
                 'John81@m.co', 'John83@m.co', 'John86@m.co', 'John88@m.co', 'John89@m.co', 'John91@m.co',
                 'John93@m.co', 'John96@m.co', 'John97@m.co'],
                ['Lily', 'Lily10@m.co', 'Lily11@m.co', 'Lily15@m.co', 'Lily18@m.co', 'Lily19@m.co', 'Lily1@m.co',
                 'Lily20@m.co', 'Lily21@m.co', 'Lily22@m.co', 'Lily26@m.co', 'Lily29@m.co', 'Lily31@m.co',
                 'Lily33@m.co', 'Lily34@m.co', 'Lily37@m.co', 'Lily38@m.co', 'Lily39@m.co', 'Lily43@m.co',
                 'Lily45@m.co', 'Lily46@m.co', 'Lily47@m.co', 'Lily49@m.co', 'Lily4@m.co', 'Lily50@m.co', 'Lily52@m.co',
                 'Lily57@m.co', 'Lily5@m.co', 'Lily60@m.co', 'Lily61@m.co', 'Lily62@m.co', 'Lily64@m.co', 'Lily66@m.co',
                 'Lily67@m.co', 'Lily68@m.co', 'Lily69@m.co', 'Lily6@m.co', 'Lily70@m.co', 'Lily71@m.co', 'Lily73@m.co',
                 'Lily74@m.co', 'Lily75@m.co', 'Lily77@m.co', 'Lily78@m.co', 'Lily7@m.co', 'Lily80@m.co', 'Lily81@m.co',
                 'Lily83@m.co', 'Lily84@m.co', 'Lily85@m.co', 'Lily88@m.co', 'Lily8@m.co', 'Lily90@m.co', 'Lily92@m.co',
                 'Lily93@m.co', 'Lily95@m.co', 'Lily96@m.co', 'Lily98@m.co'],
                ['Ethan', 'Ethan0@m.co', 'Ethan11@m.co', 'Ethan12@m.co', 'Ethan13@m.co', 'Ethan14@m.co', 'Ethan16@m.co',
                 'Ethan18@m.co', 'Ethan19@m.co', 'Ethan1@m.co', 'Ethan20@m.co', 'Ethan21@m.co', 'Ethan22@m.co',
                 'Ethan23@m.co', 'Ethan24@m.co', 'Ethan25@m.co', 'Ethan27@m.co', 'Ethan28@m.co', 'Ethan2@m.co',
                 'Ethan30@m.co', 'Ethan32@m.co', 'Ethan33@m.co', 'Ethan34@m.co', 'Ethan35@m.co', 'Ethan37@m.co',
                 'Ethan38@m.co', 'Ethan39@m.co', 'Ethan3@m.co', 'Ethan40@m.co', 'Ethan41@m.co', 'Ethan42@m.co',
                 'Ethan43@m.co', 'Ethan45@m.co', 'Ethan46@m.co', 'Ethan48@m.co', 'Ethan50@m.co', 'Ethan53@m.co',
                 'Ethan55@m.co', 'Ethan56@m.co', 'Ethan58@m.co', 'Ethan59@m.co', 'Ethan5@m.co', 'Ethan60@m.co',
                 'Ethan62@m.co', 'Ethan63@m.co', 'Ethan64@m.co', 'Ethan65@m.co', 'Ethan66@m.co', 'Ethan69@m.co',
                 'Ethan6@m.co', 'Ethan71@m.co', 'Ethan73@m.co', 'Ethan74@m.co', 'Ethan75@m.co', 'Ethan76@m.co',
                 'Ethan77@m.co', 'Ethan78@m.co', 'Ethan7@m.co', 'Ethan80@m.co', 'Ethan81@m.co', 'Ethan82@m.co',
                 'Ethan83@m.co', 'Ethan86@m.co', 'Ethan87@m.co', 'Ethan88@m.co', 'Ethan91@m.co', 'Ethan92@m.co',
                 'Ethan93@m.co', 'Ethan94@m.co', 'Ethan96@m.co', 'Ethan97@m.co', 'Ethan98@m.co', 'Ethan99@m.co',
                 'Ethan9@m.co'],
                ['Gabe', 'Gabe100@m.co', 'Gabe10@m.co', 'Gabe12@m.co', 'Gabe13@m.co', 'Gabe14@m.co', 'Gabe16@m.co',
                 'Gabe18@m.co', 'Gabe21@m.co', 'Gabe23@m.co', 'Gabe24@m.co', 'Gabe25@m.co', 'Gabe26@m.co',
                 'Gabe27@m.co', 'Gabe28@m.co', 'Gabe29@m.co', 'Gabe30@m.co', 'Gabe32@m.co', 'Gabe33@m.co',
                 'Gabe35@m.co', 'Gabe36@m.co', 'Gabe37@m.co', 'Gabe41@m.co', 'Gabe42@m.co', 'Gabe43@m.co',
                 'Gabe44@m.co', 'Gabe47@m.co', 'Gabe49@m.co', 'Gabe4@m.co', 'Gabe52@m.co', 'Gabe53@m.co', 'Gabe54@m.co',
                 'Gabe56@m.co', 'Gabe60@m.co', 'Gabe61@m.co', 'Gabe65@m.co', 'Gabe67@m.co', 'Gabe71@m.co',
                 'Gabe75@m.co', 'Gabe76@m.co', 'Gabe77@m.co', 'Gabe78@m.co', 'Gabe79@m.co', 'Gabe80@m.co',
                 'Gabe81@m.co', 'Gabe83@m.co', 'Gabe84@m.co', 'Gabe85@m.co', 'Gabe87@m.co', 'Gabe89@m.co',
                 'Gabe90@m.co', 'Gabe92@m.co', 'Gabe95@m.co', 'Gabe96@m.co', 'Gabe98@m.co', 'Gabe99@m.co',
                 'Gabe9@m.co'],
                ['Hanzo', 'Hanzo0@m.co', 'Hanzo100@m.co', 'Hanzo10@m.co', 'Hanzo12@m.co', 'Hanzo15@m.co',
                 'Hanzo16@m.co', 'Hanzo18@m.co', 'Hanzo19@m.co', 'Hanzo1@m.co', 'Hanzo20@m.co', 'Hanzo22@m.co',
                 'Hanzo23@m.co', 'Hanzo25@m.co', 'Hanzo26@m.co', 'Hanzo28@m.co', 'Hanzo2@m.co', 'Hanzo32@m.co',
                 'Hanzo35@m.co', 'Hanzo37@m.co', 'Hanzo39@m.co', 'Hanzo3@m.co', 'Hanzo42@m.co', 'Hanzo44@m.co',
                 'Hanzo45@m.co', 'Hanzo47@m.co', 'Hanzo49@m.co', 'Hanzo4@m.co', 'Hanzo51@m.co', 'Hanzo53@m.co',
                 'Hanzo55@m.co', 'Hanzo56@m.co', 'Hanzo58@m.co', 'Hanzo59@m.co', 'Hanzo62@m.co', 'Hanzo64@m.co',
                 'Hanzo65@m.co', 'Hanzo67@m.co', 'Hanzo68@m.co', 'Hanzo70@m.co', 'Hanzo71@m.co', 'Hanzo76@m.co',
                 'Hanzo79@m.co', 'Hanzo7@m.co', 'Hanzo81@m.co', 'Hanzo85@m.co', 'Hanzo86@m.co', 'Hanzo88@m.co',
                 'Hanzo89@m.co', 'Hanzo93@m.co', 'Hanzo94@m.co', 'Hanzo95@m.co', 'Hanzo97@m.co', 'Hanzo99@m.co'],
                ['Kevin', 'Kevin0@m.co', 'Kevin100@m.co', 'Kevin11@m.co', 'Kevin13@m.co', 'Kevin14@m.co',
                 'Kevin15@m.co', 'Kevin1@m.co', 'Kevin20@m.co', 'Kevin21@m.co', 'Kevin25@m.co', 'Kevin26@m.co',
                 'Kevin28@m.co', 'Kevin31@m.co', 'Kevin33@m.co', 'Kevin3@m.co', 'Kevin41@m.co', 'Kevin43@m.co',
                 'Kevin45@m.co', 'Kevin54@m.co', 'Kevin55@m.co', 'Kevin58@m.co', 'Kevin5@m.co', 'Kevin60@m.co',
                 'Kevin61@m.co', 'Kevin73@m.co', 'Kevin75@m.co', 'Kevin76@m.co', 'Kevin77@m.co', 'Kevin79@m.co',
                 'Kevin7@m.co', 'Kevin83@m.co', 'Kevin84@m.co', 'Kevin85@m.co', 'Kevin88@m.co', 'Kevin95@m.co',
                 'Kevin96@m.co', 'Kevin97@m.co', 'Kevin99@m.co'],
                ['Fern', 'Fern0@m.co', 'Fern100@m.co', 'Fern11@m.co', 'Fern13@m.co', 'Fern14@m.co', 'Fern18@m.co',
                 'Fern21@m.co', 'Fern22@m.co', 'Fern23@m.co', 'Fern24@m.co', 'Fern25@m.co', 'Fern26@m.co',
                 'Fern27@m.co', 'Fern29@m.co', 'Fern2@m.co', 'Fern31@m.co', 'Fern34@m.co', 'Fern37@m.co', 'Fern43@m.co',
                 'Fern44@m.co', 'Fern46@m.co', 'Fern47@m.co', 'Fern48@m.co', 'Fern49@m.co', 'Fern50@m.co',
                 'Fern52@m.co', 'Fern55@m.co', 'Fern58@m.co', 'Fern5@m.co', 'Fern60@m.co', 'Fern61@m.co', 'Fern62@m.co',
                 'Fern66@m.co', 'Fern68@m.co', 'Fern69@m.co', 'Fern6@m.co', 'Fern71@m.co', 'Fern74@m.co', 'Fern75@m.co',
                 'Fern77@m.co', 'Fern78@m.co', 'Fern7@m.co', 'Fern83@m.co', 'Fern84@m.co', 'Fern87@m.co', 'Fern88@m.co',
                 'Fern89@m.co', 'Fern91@m.co', 'Fern92@m.co', 'Fern94@m.co', 'Fern95@m.co', 'Fern97@m.co',
                 'Fern98@m.co', 'Fern99@m.co'],
                ['Alex', 'Alex10@m.co', 'Alex11@m.co', 'Alex14@m.co', 'Alex1@m.co', 'Alex24@m.co', 'Alex30@m.co',
                 'Alex31@m.co', 'Alex41@m.co', 'Alex46@m.co', 'Alex49@m.co', 'Alex53@m.co', 'Alex54@m.co',
                 'Alex59@m.co', 'Alex5@m.co', 'Alex67@m.co', 'Alex68@m.co', 'Alex70@m.co', 'Alex71@m.co', 'Alex74@m.co',
                 'Alex83@m.co', 'Alex87@m.co', 'Alex90@m.co', 'Alex93@m.co'],
                ['Celine', 'Celine0@m.co', 'Celine10@m.co', 'Celine12@m.co', 'Celine13@m.co', 'Celine21@m.co',
                 'Celine23@m.co', 'Celine27@m.co', 'Celine31@m.co', 'Celine32@m.co', 'Celine3@m.co', 'Celine41@m.co',
                 'Celine42@m.co', 'Celine43@m.co', 'Celine46@m.co', 'Celine49@m.co', 'Celine53@m.co', 'Celine55@m.co',
                 'Celine60@m.co', 'Celine61@m.co', 'Celine66@m.co', 'Celine67@m.co', 'Celine68@m.co', 'Celine69@m.co',
                 'Celine6@m.co', 'Celine74@m.co', 'Celine75@m.co', 'Celine76@m.co', 'Celine79@m.co', 'Celine81@m.co',
                 'Celine86@m.co', 'Celine8@m.co', 'Celine91@m.co', 'Celine96@m.co', 'Celine99@m.co']],)]
for accounts_merge in [accounts_merge_union_find, accounts_merge_dfs, ]:
    for test_accounts, expected_output in test_cases:
        assert sorted(accounts_merge(test_accounts)) == sorted(expected_output)
