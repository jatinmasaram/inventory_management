function StatsCard({
  title,
  value,
}) {

  const getAccentColor =
    () => {

      switch (title) {

        case "Products":
          return "#2563eb";

        case "Customers":
          return "#10b981";

        case "Orders":
          return "#8b5cf6";

        case "Low Stock":
          return "#ef4444";

        default:
          return "#2563eb";
      }
    };

  return (

    <div
      style={{
        backgroundColor:
          "#ffffff",

        border:
          "1px solid #e5e7eb",

        borderRadius:
          "16px",

        padding:
          "24px",

        minWidth:
          "250px",

        flex: 1,

        position:
          "relative",

        overflow:
          "hidden",

        boxShadow:
          "0 4px 12px rgba(0,0,0,0.06)",

        transition:
          "all 0.2s ease",
      }}
    >

      <div
        style={{
          position:
            "absolute",

          top: 0,

          left: 0,

          width:
            "100%",

          height:
            "5px",

          backgroundColor:
            getAccentColor(),
        }}
      />

      <p
        style={{
          margin: 0,

          color:
            "#6b7280",

          fontSize:
            "14px",

          fontWeight:
            "600",

          textTransform:
            "uppercase",

          letterSpacing:
            "0.5px",
        }}
      >
        {title}
      </p>

      <h1
        style={{
          marginTop:
            "16px",

          marginBottom:
            "8px",

          fontSize:
            "42px",

          fontWeight:
            "700",

          color:
            "#111827",
        }}
      >
        {value}
      </h1>

      <small
        style={{
          color:
            "#9ca3af",
        }}
      >
        Current Records
      </small>

    </div>
  );
}

export default StatsCard;