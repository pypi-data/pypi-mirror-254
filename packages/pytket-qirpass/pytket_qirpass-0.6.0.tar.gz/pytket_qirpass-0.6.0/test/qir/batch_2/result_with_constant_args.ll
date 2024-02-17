@0 = internal constant [5 x i8] c"Tag0\00"
@1 = internal constant [5 x i8] c"Tag1\00"

define void @program__main() #0 {
entry:
  call void @__quantum__rt__integer_record_output(i64 42, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__integer_record_output(i64 3, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @1, i32 0, i32 0))
  ret void
}

declare void @__quantum__rt__integer_record_output(i64, i8*)

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
