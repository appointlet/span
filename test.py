from unittest import main, TestCase
from datetime import datetime, timedelta
from span import Span

now = datetime.now()

class SpanTests(TestCase):    
    def test_intersects(self):
        """
        .intersects(), .lintersects(), .rintersects()
        """
        s1 = Span(now, now + timedelta(minutes=60))
        s2 = Span(now + timedelta(minutes=30), now + timedelta(minutes=90))

        self.assertTrue(s1.lintersects(s2))
        self.assertFalse(s1.rintersects(s2))
        self.assertTrue(s1.intersects(s2))

        self.assertTrue(s2.rintersects(s1))
        self.assertFalse(s2.lintersects(s1))
        self.assertTrue(s2.intersects(s1))

    def test_touches(self):
        """
        .touches(), .ltouches(), .rtouches()
        """
        s1 = Span(now, now + timedelta(minutes=60))
        s2 = Span(now + timedelta(minutes=60), now + timedelta(minutes=120))

        self.assertTrue(s1.ltouches(s2))
        self.assertFalse(s1.rtouches(s2))
        self.assertTrue(s1.touches(s2))

        self.assertFalse(s2.ltouches(s1))
        self.assertTrue(s2.rtouches(s1))
        self.assertTrue(s2.touches(s1))

    def test_encompasses(self):
        """
        .encompasses(), .encompassed_by()
        """
        s1 = Span(now, now + timedelta(minutes=60))
        s2 = Span(now + timedelta(minutes=15), now + timedelta(minutes=45))

        self.assertTrue(s1.encompasses(s2))
        self.assertFalse(s2.encompasses(s1))

        self.assertTrue(s2.encompassed_by(s1))
        self.assertFalse(s1.encompassed_by(s2))

    def test_equality(self):
        """
        .__eq__(), .__ne__()
        """
        s1 = Span(now, now + timedelta(minutes=60))
        s2 = Span(now, now + timedelta(minutes=60))
        s3 = Span(now, now + timedelta(minutes=59))

        self.assertTrue(s1 == s2)
        self.assertTrue(s1 != s3)



if __name__ == '__main__':
    main()