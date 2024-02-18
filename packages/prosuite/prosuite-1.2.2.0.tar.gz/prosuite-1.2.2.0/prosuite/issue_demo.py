import prosuite as ps

model = ps.Model("TopoModel", "D:\Test Data\ExtractStGallen.gdb")
datasets = [ps.Dataset("TLM_FLIESSGEWAESSER", model),
            ps.Dataset("TLM_STRASSE", model)]

service = ps.Service(host_name='localhost', port_nr=5151)

simpleSpecification = ps.Specification(
    name='MinimumLengthSpecification',
    description='A very simple quality specification checking feature and segment length of roads and rivers')
##
for dataset in datasets:
    simpleSpecification.add_condition(ps.Conditions.qa_min_length_0(dataset, limit=10, is3_d=False))
    simpleSpecification.add_condition(ps.Conditions.qa_segment_length_0(dataset, 1.5, False))

    envelope = ps.EnvelopePerimeter(x_min=2750673, y_min=1215551, x_max=2765845, y_max=1206640)

    out_dir = 'C:/temp/verification_output'

    verification_responses = service.verify(specification=simpleSpecification, output_dir=out_dir, perimeter=envelope)

    for verification_response in verification_responses:
        print(verification_response)