import Form from "react-bootstrap/Form";

function CheckExample() {
  return (
    <Form>
      {["checkbox", "radio"].map((type) => (
        <div key={`default-${type}`} className="mb-3">
          <Form.Check // prettier-ignore
            type={type}
            id={`default-${type}`}
            label={`default ${type}`}
          />
        </div>
      ))}
    </Form>
  );
}

export default CheckExample;
