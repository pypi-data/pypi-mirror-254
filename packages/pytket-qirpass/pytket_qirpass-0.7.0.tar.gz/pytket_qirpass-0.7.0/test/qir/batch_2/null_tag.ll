@0 = internal constant [5 x i8] c"Tag0\00"
@1 = internal constant [5 x i8] c"Tag1\00"

define void @program__main() #0 {
entry:
  %0 = add i64 1, 41
  call void @__quantum__rt__int_record_output(i64 %0, i8* null)
  ret void
}

declare void @__quantum__rt__int_record_output(i64, i8*)

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
