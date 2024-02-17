@0 = internal constant [5 x i8] c"Tag0\00"
@1 = internal constant [5 x i8] c"Tag1\00"

define void @program__main() #0 {
entry:
  %0 = add i64 1, 41
  %1 = add i64 1, 2
  call void @__quantum__rt__int_record_output(i64 %0, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @0, i32 0, i32 0))
  %2 = icmp eq i64 %0, %1
  br i1 %2, label %then, label %else
then:
  %3 = add i64 %1, 1
  br label %exit
else:
  %4 = add i64 %1, 2
  br label %exit
exit:
  %5 = phi i64 [ %3, %then ],  [ %4, %else ]
  call void @__quantum__rt__int_record_output(i64 %5, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @1, i32 0, i32 0))
  ret void
}

declare void @__quantum__rt__int_record_output(i64, i8*)

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
