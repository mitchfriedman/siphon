def get_args(parser, request):
    extra_args = _get_extra_params(request)
    args = parser.parse_args(strict=False)
    args.update(extra_args)

    return args

def _get_extra_params(request):
    return request.form.to_dict()
