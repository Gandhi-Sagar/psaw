from psaw import PushshiftAPI, PushshiftAPIMinimal
import pytest
import copy


class BaseTests(object):

    @pytest.mark.parametrize("rate_limit", [-2.5, -1, 0, 0.5, None, 'foo'])
    def test_minimum_rate_limit(self, rate_limit):
        with pytest.raises((AssertionError,TypeError)):
            self.cls(rate_limit=rate_limit)

    #def test_limited(self):
    #    payload=['aggs']
    #    assert self.api._limited(payload)
    ### No idea what's going on here...

    @pytest.mark.parametrize("kind", ['comment', 'submission'])
    def test_wrap_thing(self, kind):
        thing = {'foo':1, 'bar':'baz', 'created_utc':0}
        w = self.api._wrap_thing(copy.deepcopy(thing), kind)
        
        assert kind in str(type(w))
        for k,v in thing.items():
            assert getattr(w, k) == v
            print(w.d_, k)
            assert w.d_[k] == v



# There should be able to do this with pytest.mark.parameterize
class TestAPI(BaseTests):

        def setup(self):
            self.cls = PushshiftAPI
            self.api = self.cls()


class TestAPIMinimal(BaseTests):

        def setup(self):
            self.cls = PushshiftAPIMinimal
            self.api = self.cls()
