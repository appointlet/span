class Span(object):
    """
    Helper for determining basic relationships between datetime ranges.
    """

    def __init__(self, start, end): 
        self.start = start
        self.end = end
    
    def intersects(self, span):
        """
        Returns true if this span intersects with a given span
        """
        return self.lintersects(span) or self.rintersects(span)

    def lintersects(self, span):
        """
        If this span intersects the left (starting) side of the given span.
        """
        if isinstance(span, list):
            return [sp for sp in span if self._lintersects(sp)]

        return self._lintersects(span)

    _lintersects = lambda self, span: self.start < span.start < self.end < span.end

    def rintersects(self, span):
        """
        If this span intersects the right (ending) side of the given span.
        """
        if isinstance(span, list):
            return [sp for sp in span if self._rintersects(sp)]

        return self._rintersects(span)

    _rintersects = lambda self, span: span.start < self.start < span.end < self.end

    def touches(self, span):
        """
        Returns true if this span touches the given span.
        """
        return self.ltouches(span) or self.rtouches(span)

    def ltouches(self, span):
        """
        Returns true if the end of this span touches the left (starting) side of the given span.
        """
        if isinstance(span, list):
            return [sp for sp in span if self._ltouches(sp)]

        return self._ltouches(span)

    _ltouches = lambda self, span: self.end == span.start

    def rtouches(self, span):
        """
        Returns true if the start of this span touches the right (ending) side of the given span.
        """
        if isinstance(span, list):
            return [sp for sp in span if self._rtouches(sp)]

        return self._rtouches(span)

    _rtouches = lambda self, span: self.start == span.end
    
    def encompasses(self, span):
        """
        Returns true if the given span fits inside this one
        """
        if isinstance(span, list):
            return [sp for sp in span if self._encompasses(sp)]

        return self._encompasses(span)
    
    _encompasses = lambda self, span: self.start <= span.start < span.end <= self.end

    def encompassed_by(self, span):
        """
        Returns true if the given span encompasses this span.
        """
        if isinstance(span, list):
            return [sp for sp in span if sp.encompasses(self)]

        return span.encompasses(self)

    def __eq__(self, span):
        return self.start == span.start and self.end == span.end
    
    def __ne__(self, span):
        return not self.__eq__(span)

    def __unicode__(self):
        return ' - '.join([self.start.isoformat(), self.end.isoformat()])

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __repr__(self):
        return unicode(self)