# coding: utf-8


def xinshi_only():
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.session.get('xinshi') == 'i_am_xinshi':
                return view_func(request, *args, **kwargs)
            else:
                raise
        return _wrapped_view
    return decorator