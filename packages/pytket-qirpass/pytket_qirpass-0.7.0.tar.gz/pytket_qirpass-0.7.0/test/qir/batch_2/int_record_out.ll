define void @program__main() #0 {
entry:
  call void @__quantum__rt__int_record_output(i64 3)
  call void @__quantum__rt__bool_record_output(i1 1)
  ret void
}

declare void @__quantum__rt__int_record_output(i64)
declare void @__quantum__rt__bool_record_output(i1)
attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
