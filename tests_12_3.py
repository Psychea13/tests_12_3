from unittest import TestCase, skipIf


class Runner:

    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest(TestCase):

    is_frozen = False

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('Бегун')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Бегун')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = Runner('Бегун 1')
        runner_2 = Runner('Бегун 2')
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


class Tournament:

    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class TournamentTest(TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usain = Runner('Усэйн', 10)
        self.Andrey = Runner('Андрей', 9)
        self.Nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for results in cls.all_results.values():
            formated = {place: str(runner) for place, runner in results.items()}
            print(formated)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        tournament = Tournament(90, self.Usain, self.Nick)
        results = tournament.start()
        TournamentTest.all_results[1] = results
        self.assertEqual('Ник', results[2].name)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        tournament = Tournament(90, self.Andrey, self.Nick)
        results = tournament.start()
        TournamentTest.all_results[2] = results
        self.assertEqual('Ник', results[2].name)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        tournament = Tournament(90, self.Usain, self.Andrey, self.Nick)
        results = tournament.start()
        TournamentTest.all_results[3] = results
        self.assertEqual('Ник', results[3].name)


if __name__ == '__main__':
    main()
