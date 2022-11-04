import unittest

from app.core.tasks import task_factory


class TaskTest(unittest.TestCase):
    def setUp(self) -> None:
        self.task = 'Unknown Task'

    def test_task_factory(self):
        with self.assertRaises(NotImplementedError) as context:
            task_factory(self.task)
        self.assertTrue('This task is not available.' in context.exception.args)


if __name__ == '__main__':
    unittest.main()
