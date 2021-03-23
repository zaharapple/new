from models import Employee, Recruiter, Programmer, Candidate, Vacancy


def main():
    r = Recruiter("Sasha", 150, 21, 'sasha@com')
    p = Programmer("Slava", 220, 23, 'sl@com', {'have a car ', 'Python', 'JS', 'Git', 'HTML'})
    p2 = Programmer("Kostya", 200, 24, 'kos@com', {'know of English ', 'Python', 'Django'})
    c = Candidate("Petya", "Razrabotka", "JS", "pet@com", "trenie")
    c2 = Candidate("Katya", "Recruter", "English", "KET@com", "С1")
    c3 = Candidate("Kiril", "Razrabotkbotka", "Python", "Kir@com", "junior")
    v = Vacancy("Programmer", "Python,JS,HTML", "junior")
    v2 = Vacancy("Recruiter", "комуникабельность , знание английского языка", "стаж 1год")

    # print(v)
    # print(v2)
    #
    # print('---------------------------')
    #
    # print(c)
    # print(c.work())
    # print(c2)
    # print(c3)
    #
    # print('---------------------------')
    #
    # print(r)
    # print(r.work())
    # print(r.cheak_salary())
    #
    # print('---------------------------')
    #
    # print(p)
    # print(p.work())
    # print(p.cheak_salary())
    # print(p.tech_stack)
    #
    # print('---------------------------')
    # print(r == p)  # comparison by salary
    # print('---------------------------')
    #
    # print(p2)
    # print(p2.work())
    # print(p2.cheak_salary())
    # print(p2.tech_stack)
    #
    # print('---------------------------')
    # print(p > p2)
    # print()

    alfaprogr = p + p2
    print(alfaprogr)
    print(alfaprogr.work())
    print(alfaprogr.cheak_salary())
    print(alfaprogr.tech_stack)


if __name__ == '__main__':
    main()
